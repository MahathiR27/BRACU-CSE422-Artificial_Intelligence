import math
from heapq import *

in_f = open("input.txt", 'r')

v,e = map(int, in_f.readline().split())
v+=1

graph = {i:[] for i in range(1,v)}
in_f.readline()

start,goal = map(int,in_f.readline().split())
in_f.readline()

h = {}
for i in range(1,v):
  h[i] = int(in_f.readline().split()[1])
in_f.readline()

for i in range(e):
  a,b = map(int,in_f.readline().split())
  graph[a].append(b)
  graph[b].append(a)

# print(f'''Start: {s}; Goal: {g}
# Heuristic: {h}
# Graph: {graph}''')

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

print("Actual Cost for each node to reach goal:", actual_cost)