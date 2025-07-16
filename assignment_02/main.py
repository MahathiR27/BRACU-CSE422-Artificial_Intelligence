import random

grid = (25,25)
blocks = ("ALU", "Cache", "Control Unit", "Register File", "Decoder", "Floating Unit")
dim = {"ALU":(5,5), "Cache":(7,4), "Control Unit":(4,4), "Register File":(6,6), "Decoder":(5,3), "Floating Unit":(5,5)}
connections = ((3,0), (2,0), (0,1), (3,5), (1,4), (4,5))

def grid_checker(co_ordinate,block_num):
  block = blocks[block_num]
  
  x = co_ordinate[0]
  y = co_ordinate[1]
  
  x_add = dim[block][0]
  y_add = dim[block][1]
  
  if x<0 or y<0 or x+x_add>grid[0] or y+y_add>grid[1]:
    return False
  return True

print(grid_checker([20,20],0))