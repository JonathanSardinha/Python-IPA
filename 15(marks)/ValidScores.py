def validateScore(num):
 if 0 < num <= 100:
  return True
 else:
  return False

def findValidScores(lst_num):
 lst = []
 for i in lst_num:
  if validateScore(i) == True :
   lst.append(i)

 if lst == []:
  print("No valid score found")
 else:
  print(f'Valid Scores = {lst}')

n = int(input())
lst_num = []
for i in range(n):
 num = int(input())
 lst_num.append(num)

findValidScores(lst_num)
 