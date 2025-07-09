from heapq import *

in_f = open("input.txt", 'r')

d = tuple(map(int, in_f.readline().split())) # Dimension of the maze

start = tuple(map(int, in_f.readline().split()))
goal = tuple(map(int, in_f.readline().split()))

maze = []
for i in range(d[0]):
  a = [i for i in in_f.readline()]
  if a[-1] not in ["#","0"]: # Removing "\n" in the end
    a.pop(-1) 

  maze.append(a)

# for i in maze:
#   print(i)

def gen_h(node): # Generate manhattan distance
  x1,y1 = node
  x2,y2 = goal
  return abs(x1-x2)+abs(y1-y2)

queue = []
heappush(queue,(gen_h(start),0,start,[]))

visited = []

def valid(node): # node ki adow valid?
  x,y = node
  if node not in visited and x>=0 and y>=0 and x<d[0] and y<d[1] and maze[x][y]=='0':
    return True
  return False

maybe_paths = {}

def all_paths(node): # All possible ways to go from a node
  nodes_to_go = []

  x,y = node

  down = (x+1,y)
  left = (x,y-1)
  right = (x,y+1)

  if valid(down):
    maybe_paths[down] = 'D'
    nodes_to_go.append(down)

  if valid(left):
    maybe_paths[left] = 'L'
    nodes_to_go.append(left)

  if valid(right):
    maybe_paths[right] = 'R'
    nodes_to_go.append(right)

  return nodes_to_go

def a_star(queue):
  if len(queue) == 0:
    return -1
  else:
    h, cost, node, path = heappop(queue)
    visited.append(node)
    # print(node)
    # print(queue)
    if node == goal:
      return path

    for new_node in all_paths(node): # Oi node theke dane bame niche joto jawar jayga ase check kore list e add kortese
      new_cost = cost + 1 # Sob node er cost parent node er cost theke 1 beshi.
      h_new = gen_h(new_node) + new_cost
      heappush(queue,(h_new,cost,new_node,path + [maybe_paths[new_node]])) # Existing jei path ase oi path er sathe new dhore ana node add
# Basically jei node jei path ei jak shei path e nije nije store korbe and goal e jei node reach korbe oitar path return korbo
    return a_star(queue)

res = a_star(queue)
if res != -1:
  print(len(res))
  print("".join(res))
else:
  print(-1)