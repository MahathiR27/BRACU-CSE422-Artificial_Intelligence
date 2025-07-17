import random
import math

grid = (25,25)
blocks = ("ALU", "Cache", "Control Unit", "Register File", "Decoder", "Floating Unit")
dim = {"ALU":(5,5), "Cache":(7,4), "Control Unit":(4,4), "Register File":(6,6), "Decoder":(5,3), "Floating Unit":(5,5)}
connections = ((3,0), (2,0), (0,1), (3,5), (1,4), (4,5)) # Kon index er component er sathe kon index er component connect korte hobe

overlap_penalty, wiring_penalty = 1000, 2

p_population = []
c_population = []
parent_f = []
child_f = []

def grid_checker(co_ordinate,block_num): # block_num = component er index number to get the dimension
  block = blocks[block_num]
  x, y = co_ordinate
  x_add, y_add = dim[block] # Hight, Width
  
  if x+x_add>grid[0] or y+y_add>grid[1]: 
    return False
  return True

def generate_node(block_num): # Random ekta generate korbe and block_number wise grid_checker marbe false ashle recurs
  node = (random.randint(0,25), random.randint(0,25))
  if grid_checker(node,block_num):
    return node
  #print("Regenerate")
  return generate_node(block_num)

def overlap(node1,block_num1,node2,block_num2):
  block1, block2 = blocks[block_num1], blocks[block_num2] # kona kon component
  
  x1, y1 = node1 # LB Coordinate
  x2, y2 = node2
  
  x1_add, y1_add = dim[block1] #Hight, Width
  x2_add, y2_add = dim[block2]
  
  a_left = x1
  b_left = x2
  a_right = x1+x1_add
  b_right = x2+x2_add
  a_bottom = y1
  b_bottom = y2
  a_top = y1+y1_add
  b_top = y2+y2_add

  overlap = not (a_right <= b_left or a_left >= b_right or a_bottom >= b_top or a_top <= b_bottom) # copy

  return overlap

def wire(cromo): #Center to center wire distance
  wire_distance = 0
  for c in connections:
    i, j = c
    
    block1, block2 = blocks[i], blocks[j]
    
    x1, y1 = cromo[i] # LB Coordinate
    x2, y2 = cromo[j]
    
    x1_add, y1_add = dim[block1] #Hight, Width
    x2_add, y2_add = dim[block2]
    
    center1 = (x1+x1_add/2, y1+y1_add/2)
    center2 = (x2+x2_add/2, y2+y2_add/2)
    
    wire_distance += math.sqrt((center2[0]-center1[0])**2+(center2[1]-center1[1])**2) #sqrt((x2 - x1)**2 + (y2 - y1)**2)
  
  return wire_distance

def box(cromo):
  x_max, y_max = cromo[0]
  x_min, y_min = cromo [0]
  
  for i in cromo:
    if i[0] > x_max:
      x_max = i[0]
    elif i[0] < x_min:
      x_min = i[0]
    
    if i[1] > y_max:
      y_max = i[1]
    elif i[1] < y_min:
      y_min = i[1]
  
  return (x_max - x_min) * (y_max - y_min) # Copy

def fitness(cromo, output = False):
  # Count overlap count of a cromo
  overlap_count = 0
  for i in range (0,5):
    for j in range (i+1,6):
      if overlap(cromo[i],i,cromo[j],j):
        overlap_count+=1
        #print(f"Overlap: {blocks[i]} {cromo[i]}, {blocks[j]} {cromo[j]}")

  wire_distance = round(wire(cromo),2)
  bounding_box = box(cromo)
  
  fitness_value = -(overlap_penalty*overlap_count + wiring_penalty*wire_distance + bounding_box)
  
  child_f.append((fitness_value,cromo))
  
  if output:
    print("the total overlap counts:",overlap_count)
    print("total wiring length:",wire_distance)
    print("the total bounding box area",bounding_box)
    print("best total fitness value:",fitness_value)
    print("optimal placement of bottom-left coordinates:", cromo)

def cross(temp_population):
  point = random.randint(1,5)
  random.shuffle(temp_population)
  new_population = []
  
  i = 0
  while i < 6: # Shuffled parent and er porer ta diye off spring
    new_cromo1 = temp_population[i][:point] + temp_population[i+1][point:]
    new_cromo2 = temp_population[i+1][:point] + temp_population[i][point:]
    
    new_population.append(new_cromo1)
    new_population.append(new_cromo2)

    i+=2
    
  # print("Crossed")
  
  return new_population

def mutate(temp_population):
  if 5 <= random.randint(0,100) <= 10:
    cromo = temp_population[random.randint(0,5)]
    gene = random.randint(0,5)
    cromo[gene] = generate_node(gene)
    
    # print("Mutated")
  return temp_population

def main():
  global p_population, c_population, parent_f, child_f
  
  for gen in range (15):
    if len(p_population) != 0: # Sob gula element same hoye gele plateau
      plateu = True
      tester = p_population[0]
      
      for i in p_population:
        if tester != i:
          plateu = False

      if plateu:
        return p_population[0] # plateau hoise just return any cromo 

    for cromo in c_population: # Fitness check
      fitness(cromo)
    
    if len(p_population) == 0: # Jodi Parent na thake no need for elitism
      p_population = c_population.copy()
      c_population = mutate(cross(p_population))
    
    else: # Elitism
      stupid_child = sorted(child_f)[0] # Sort korle only key value gula Ascending order hoye jay
      elite_parent = sorted(parent_f)[-1]
      
      c_population.remove(stupid_child[1])
      c_population.append(elite_parent[1])
    
      p_population = c_population.copy()
      c_population = mutate(cross(p_population))
    
    # Next generation dhorar age mane this gen parents
    parent_f = child_f.copy() # Child der parent banaye diye child reset
    child_f = []
    
  return sorted(parent_f)[-1][1] #15 ta iteration sesh hoile just result the cromo with best fitness. 

for j in range (6): # Creating start population
  x = []
  for i in range (6):
    x.append(generate_node(i))
  c_population.append(x)


fitness(main(),True)