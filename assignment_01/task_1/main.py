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
heappush(queue,(gen_h(start), start))

visited = []
path = []

def valid(node): # node ki adow valid?
  x,y = node
  if node not in visited and x>=0 and y>=0 and x<d[0] and y<d[1] and maze[x][y]=='0':
    return True
  return False

def all_paths(node): # All possible ways to go from a node
  paths = {}
  x,y = node

  down = (x+1,y)
  left = (x,y-1)
  right = (x,y+1)

  if valid(down):
    paths['D'] = down

  if valid(left):
    paths['L'] = left

  if valid(right):
    paths['R'] = right
  
  return paths


def a_star(queue):
  if len(queue) == 0:
    return -1
  else:
    h, node = heappop(queue)
    visited.append(node)
    #print(visited)
    if node == goal:
      return 1

    for direction, new_node in all_paths(node).items():
      h_new = gen_h(new_node) + 1
      heappush(queue,(h_new,new_node))

    return a_star(queue)

print(a_star(queue))