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

for i in maze:
  print(i)