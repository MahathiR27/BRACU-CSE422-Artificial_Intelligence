in_f = open("input.txt", 'r')

all_nuces = [i for i in in_f.readline().strip().split(",")]
target = in_f.readline().strip()
std_id = list(map(int, in_f.readline().strip().split()))[-len(target):]

def minimax(nuces, sequence=''):
  if len(sequence) == len(all_nuces):
    # Utility
    return utility_gen(sequence)
  else:
    for i in nuces:
      next_nuces = nuces.copy() # Copy create kore jeta already add kora hoye gese oita remove kore diye baki tar upor recursion
      next_nuces.remove(i)
  
      utility = minimax(next_nuces, sequence + i) # loop er element ta ke sequence e add kore recurssion e send kortese

def utility_gen(temp_sequence):
  sequence_len = len(temp_sequence) - len(target)
  sum = 0
  print(temp_sequence)
  print(target)
  print(sequence_len)
  
  if sequence_len == 0: # Sob gula thik thak moto thakle id*(new-target)
    for i in range(len(temp_sequence)):
      sum -= std_id[i]*abs(ord(temp_sequence[i])-ord(target[i]))
  
  elif sequence_len > 0: # Sequence jodi boro hoy
    for i in range (sequence_len):
      sum -= std_id[i]*abs(ord(temp_sequence[i])-ord(target[i]))
    
    for i in temp_sequence[len(target):]: # Target er len er por theke baki sequence sum e nitese
      sum -= ord(i)
      
  else:
    for i in range (abs(sequence_len)):
      sum -= std_id[i]*abs(ord(temp_sequence[i])-ord(target[i]))
    
    for i in target[len(temp_sequence):]: # Sequence er len er por theke baki target sum e nitese
      sum -= ord(i)
  
  return sum

minimax(all_nuces)