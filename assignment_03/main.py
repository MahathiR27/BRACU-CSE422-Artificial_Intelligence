in_f = open("input.txt", 'r')

all_nuces = [i for i in in_f.readline().strip().split(",")]
target = in_f.readline().strip()
std_id = list(map(int, in_f.readline().strip().split()))[-len(target):]

def minimax(nuces, sequence=''):
  if len(sequence) == len(all_nuces):
    # Utility
    print(sequence)
    sequence = ''
    return
  else:
    for i in nuces:
      next_nuces = nuces.copy()
      next_nuces.remove(i)
  
      minimax(next_nuces, sequence + i)

minimax(all_nuces)