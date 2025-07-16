import random

grid = (25,25)
blocks = ("ALU", "Cache", "Control Unit", "Register File", "Decoder", "Floating Unit")
dim = {"ALU":(5,5), "Cache":(7,4), "Control Unit":(4,4), "Register File":(6,6), "Decoder":(5,3), "Floating Unit":(5,5)}
connections = ((3,0), (2,0), (0,1), (3,5), (1,4), (4,5)) # Kon index er component er sathe kon index er component connect korte hobe

population = []
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

  overlap = not (a_right <= b_left or a_left >= b_right or a_bottom >= b_top or a_top <= b_bottom)

  return overlap

def ga(population):
  for cromo in population:
    for i in range (0,5):
      for j in range (i+1,6):
        if overlap(cromo[i],i,cromo[j],j):
          print(f"Overlap: {blocks[i]} {cromo[i]}, {blocks[j]} {cromo[j]}")

for j in range (6): # Creating start population
  x = []
  for i in range (6):
    x.append(generate_node(i))
  population.append(x)

for i in population:
  print(i)

# population = [[(9, 6), (7, 12), (1, 0), (10, 9), (16, 6), (16, 5)],
# [(18, 19), (15, 14), (19, 17), (10, 3), (11, 20), (3, 17)],
# [(9, 17), (8, 4), (4, 20), (10, 10), (2, 5), (20, 15)],
# [(19, 9), (17, 14), (0, 9), (16, 19), (4, 10), (16, 4)],
# [(17, 18), (13, 2), (5, 19), (12, 19), (20, 0), (7, 7)],
# [(18, 0), (9, 2), (6, 17), (6, 9), (0, 20), (0, 13)]]

ga(population)