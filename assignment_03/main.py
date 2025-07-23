in_f = open("input.txt", 'r')

all_nuces = [i for i in in_f.readline().strip().split(",")]
target = in_f.readline().strip()
std_id = list(map(int, in_f.readline().strip().split()))[-len(target):]

def minimax(nuces, sequence=''):
  if len(sequence) == len(all_nuces):
    # Utility
    x = utility_gen(sequence)
    print(x)
    print(sequence)
    sequence = ''
    return x
  else:
    for i in nuces:
      next_nuces = nuces.copy() # Copy create kore jeta already add kora hoye gese oita remove kore diye baki tar upor recursion
      next_nuces.remove(i)
  
      utility = minimax(next_nuces, sequence + i) # loop er element ta ke sequence e add kore recurssion e send kortese

def utility_gen(temp_sequence):
  sequence_len = len(temp_sequence)
  sum = 0
  
  if sequence_len == len(target):
    for i in range(sequence_len):
      sum -= std_id[i]*abs(ord(temp_sequence[i])-ord(target[i]))
  return sum

minimax(all_nuces)