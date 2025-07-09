import math
from heapq import *

in_f = open("input.txt", 'r')

v,e = map(int, in_f.readline().split()) # No of vertex and edges
v+=1

graph = {i:[] for i in range(1,v)} # Graph er empty dict
in_f.readline()

start,goal = map(int,in_f.readline().split())
in_f.readline()

h = {} 
for i in range(1,v): # Adding the heuristic values in dict
  h[i] = int(in_f.readline().split()[1])
in_f.readline()

for i in range(e): # Adding edges in the graph dict
  a,b = map(int,in_f.readline().split())
  graph[a].append(b)
  graph[b].append(a)

# print(f'''Start: {s}; Goal: {g}
# Heuristic: {h}
# Graph: {graph}''')

# Dijkstra Algo starting from goal to find all g(n)
actual_cost = {i:math.inf for i in range(1,v)}
queue = []

actual_cost[goal] = 0
heappush(queue,(0, goal))

def dijkstra(queue):
  if len(queue) == 0:
    return actual_cost
  else:
    w, v = heappop(queue)
    for neighbor in graph[v]:
      path_cost = w + 1
      if path_cost < actual_cost[neighbor]:
        actual_cost[neighbor] = path_cost
        heappush(queue,(path_cost, neighbor))
    return dijkstra(queue)

dijkstra(queue)

not_admissible = []

for i in graph.keys():
  if h[i] > actual_cost[i]: # To be admissible, h(n) <= g(n)
    not_admissible.append(str(i))

if len(not_admissible) == 0:
  print(1)
else:
  print(f"0\n\nHere nodes {",".join(not_admissible)} are inadmissible.")