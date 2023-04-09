def Position(lst,stri):
 for i,v in enumerate(lst):
  if v == stri:
   return i
   break
 else:
   return("String Not Found")

n = int(input())
lst = []
for i in range(n):
 string = input()
 lst.append(string)

stri = input()

res = Position(lst,stri)
print(res)