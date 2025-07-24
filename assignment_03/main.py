import math

in_f = open("input.txt", 'r')

all_nuces = [i for i in in_f.readline().strip().split(",")]
target = in_f.readline().strip()
std_id = list(map(int, in_f.readline().strip().split()))

s_id = std_id[:2]
s_id = int(str(s_id[0])+str(s_id[1]))/100

std_id = std_id[-len(target):]

sequence = ''
alpha = -math.inf
beta = math.inf

def minimax(nuces, sequence, alpha, beta, max_player):
  if len(sequence) == len(all_nuces):
    # Utility
    s_pos = sequence.find("S")
    if s_pos != -1 and s_pos % 2 == 0: # Max player er always even position e pore move
      return s_utility_gen(sequence, s_pos), sequence 
    else:
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
    for i in range (len(target)):
      sum -= std_id[i]*abs(ord(temp_sequence[i])-ord(target[i]))
    
    for i in temp_sequence[len(target):]: # Target er len er por theke baki sequence sum e nitese
      sum -= ord(i)
      
  else:
    for i in range (len(temp_sequence)):
      sum -= std_id[i]*abs(ord(temp_sequence[i])-ord(target[i]))
    
    for i in target[len(temp_sequence):]: # Sequence er len er por theke baki target sum e nitese
      sum -= ord(i)
  
  return sum

def s_utility_gen(temp_sequence,s_pos):
  sequence_len = len(temp_sequence) - len(target)
  sum = 0
  weight = std_id.copy()
  
  for i in range(s_pos,len(weight)):
    weight[i] *= s_id

  if sequence_len == 0: # Sob gula thik thak moto thakle id*(new-target)
    for i in range(len(temp_sequence)):
      sum -= weight[i]*abs(ord(temp_sequence[i])-ord(target[i]))
  
  elif sequence_len > 0: # Sequence jodi boro hoy
    for i in range(len(target)):
      sum -= weight[i]*abs(ord(temp_sequence[i])-ord(target[i]))
    
    for i in temp_sequence[len(target):]: # Target er len er por theke baki sequence sum e nitese
      sum -= ord(i)
      
  else:
    for i in range(len(temp_sequence)): 
      sum -= weight[i]*abs(ord(temp_sequence[i])-ord(target[i]))
    
    for i in target[len(temp_sequence):]: # Sequence er len er por theke baki target sum e nitese
      sum -= ord(i)

  return sum


# Task 1 - Comment out task 2 to get proper outputs.
utility, sequence = minimax(all_nuces,sequence,alpha,beta, max_player = True)

print("Best gene sequence generated:", sequence)
print("Utility Score:", utility)

# Task 2 - Comment out the Task 1 function call and uncomment the following part

# utility, sequence = minimax(all_nuces,sequence,alpha,beta, max_player = True)

# sequence = ''
# alpha = -math.inf
# beta = math.inf
# all_nuces.append("S")
# s_utility, s_sequence = minimax(all_nuces,sequence,alpha,beta, max_player = True)

# if s_utility > utility:
#   print("YES")
# else:
#   print("NO")

# print(f'''With special nucleotide
# Best gene sequence generated: {s_sequence}, Utility score: {s_utility}''')