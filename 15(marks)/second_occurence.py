def getIndex(lst,num):
 k=0
 for i,v in enumerate(lst):
  if v == num:
   k += 1
   if k == 2:
    return i
    break
  
 return 0
 

n = int(input())
lst = []
for i in range(n):
 num1 = int(input())
 lst.append(num1)

num = int(input())

print()
sol = getIndex(lst,num)
print(sol)