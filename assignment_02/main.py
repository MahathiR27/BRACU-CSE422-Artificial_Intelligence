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
  
  x = co_ordinate[0]
  y = co_ordinate[1]
  
  x_add = dim[block][0] # Hight
  y_add = dim[block][1] # Width
  
  if x+x_add>grid[0] or y+y_add>grid[1]: 
    return False
  return True

def generate_node(block_num): # Random ekta generate korbe and block_number wise grid_checker marbe false ashle recurs
  node = (random.randint(0,25), random.randint(0,25))
  if grid_checker(node,0):
    return node
  #print("Regenerate")
  return generate_node(block_num)

for j in range (6): # Creating start population
  x = []
  for i in range (6):
    x.append(generate_node(i))
  population.append(x)

for i in population:
  print(i)