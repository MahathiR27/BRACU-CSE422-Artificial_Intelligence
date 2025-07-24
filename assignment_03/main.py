import math

in_f = open("input.txt", 'r')

all_nuces = [i for i in in_f.readline().strip().split(",")]
target = in_f.readline().strip()
std_id = list(map(int, in_f.readline().strip().split()))[-len(target):]

sequence = ''
alpha = -math.inf
beta = math.inf

def minimax(nuces, sequence, alpha, beta, max_player):
  if len(sequence) == len(all_nuces):
    # Utility
    return utility_gen(sequence), sequence # Tree er ekdom last e jaye full seq pawar pore utility calc korbe
  
  elif max_player:
    max_eval = -math.inf # Initial value to check if the new utility is max or not
    result = ''
    for i in nuces:
      next_nuces = nuces.copy() # Copy create kore jeta already add kora hoye gese oita remove kore diye baki tar upor recursion
      next_nuces.remove(i)
  
      utility, updated_sequence = minimax(next_nuces, sequence + i, alpha, beta,not max_player) # loop er element ta ke sequence e add kore recurssion e send kortese
# Full sequence pawar pore oitar utility and oi sequence ta store kortese
      if utility > max_eval: # Max vlaue update kortese
        max_eval = utility
        result = updated_sequence
      
      alpha = max(alpha, utility)
      if alpha >= beta:
        break
      
    return max_eval, result
  else:
    min_eval = math.inf
    result = ''
    for i in nuces:
      next_nuces = nuces.copy() # Copy create kore jeta already add kora hoye gese oita remove kore diye baki tar upor recursion
      next_nuces.remove(i)
  
      utility, updated_sequence = minimax(next_nuces, sequence + i, alpha, beta,not max_player) # loop er element ta ke sequence e add kore recurssion e send kortese
      
      if utility < min_eval: 
        min_eval = utility
        result = updated_sequence
      
      beta = min(beta,utility)
      
      if alpha >= beta:
        break
      
    return min_eval, result
def utility_gen(temp_sequence):
  sequence_len = len(temp_sequence) - len(target)
  sum = 0
  
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

utility, sequence = minimax(all_nuces,sequence,alpha,beta, max_player = True)

print("Best gene sequence generated:", sequence)
print("Utility Score:", utility)