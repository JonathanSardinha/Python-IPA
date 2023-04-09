def count_str(lst_string, target):
 c = 0 
 for i in lst_string:
  c += i.lower().count(target.lower())
 return c

n = int(input())
lst_string = []
for i in range(n):
 string  = input()
 lst_string.append(string)

target = input()

res = count_str(lst_string, target)
if res:
 print(res)
else:
 print('No string found')


