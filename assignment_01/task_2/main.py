in_f = open("input.txt", 'r')

v,e = map(int, in_f.readline().split())
v+=1

graph = {i:[] for i in range(1,v)}
in_f.readline()

s,g = map(int,in_f.readline().split())
in_f.readline()

h = {}
for i in range(1,v):
  h[i] = int(in_f.readline().split()[1])
in_f.readline()

for i in range(e):
  a,b = map(int,in_f.readline().split())
  graph[a].append(b)
  graph[b].append(a)

print(f'''Start: {s}; Goal: {g}
Heuristic: {h}
Graph: {graph}''')