import random
import math

grid = (25,25)
blocks = ("ALU", "Cache", "Control Unit", "Register File", "Decoder", "Floating Unit")
dim = {"ALU":(5,5), "Cache":(7,4), "Control Unit":(4,4), "Register File":(6,6), "Decoder":(5,3), "Floating Unit":(5,5)}
connections = ((3,0), (2,0), (0,1), (3,5), (1,4), (4,5)) # Kon index er component er sathe kon index er component connect korte hobe

overlap_penalty, wiring_penalty = 1000, 2

p_population = []
c_population = []
parent_f = {}
child_f = {}

def grid_checker(co_ordinate,block_num): # block_num = component er index number to get the dimension
  block = blocks[block_num]
  x, y = co_ordinate
  x_add, y_add = dim[block] # Hight, Width
  
  if x+x_add>grid[0] or y+y_add>grid[1]: 
    return False
  return True

def generate_node(block_num): # Random ekta generate korbe and block_number wise grid_checker marbe false ashle recurs
  node = (random.randint(0,25), random.randint(0,25))
  if grid_checker(node,0):
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

def wire(cromo):
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


def fitness(cromo):
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
  
  child_f[fitness_value] = cromo
  
  # print("Overlap:",overlap_count)
  # print("Wire Distance:",wire_distance)
  # print("Bounding Box:",bounding_box)
  # print("Fitness value:",fitness_value)

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

def ga(tmep_population):
  global p_population
  global c_population
  
  for gen in range (2):
    for cromo in tmep_population:
      fitness(cromo)
    
    if len(p_population) == 0: # Jodi Parent na thake no need for elitism
      p_population = c_population.copy()
      c_population = cross(p_population)

for j in range (6): # Creating start population
  x = []
  for i in range (6):
    x.append(generate_node(i))
  c_population.append(x)

# for i in c_population:
#   print(i)

# c_population = [[(9, 6), (7, 12), (1, 0), (10, 9), (16, 6), (16, 5)],
# [(18, 19), (15, 14), (19, 17), (10, 3), (11, 20), (3, 17)],
# [(9, 17), (8, 4), (4, 20), (10, 10), (2, 5), (20, 15)],
# [(19, 9), (17, 14), (0, 9), (16, 19), (4, 10), (16, 4)],
# [(17, 18), (13, 2), (5, 19), (12, 19), (20, 0), (7, 7)],
# [(18, 0), (9, 2), (6, 17), (6, 9), (0, 20), (0, 13)]]

ga(c_population)