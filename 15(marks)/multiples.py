def FindMultiples(m):
 c = 0
 for i in l:
  if(i % m == 0):
   c = c + 1
 return c

n = int(input())
l=[]
for i in range(n):
 e = int(input())
 l.append(e)

m = int(input())
c = FindMultiples(m)
if c == 0:
 print("Multiples not found")
else:
 print("Number of Multiples of passed integer:",c)