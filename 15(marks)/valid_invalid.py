def check(string):
 return all(char.isalpha() or char.isspace() for char in string)

n = int(input())
lst = []
for i in range(n):
 string = input()
 lst.append(string)

valid = 0
invalid = 0

for i in lst:
 res = check(i)
 if res == True:
  valid += 1
 else:
  invalid +=1

print(f"Count of Valid strings = {valid}\nCount of Invalid Stirngs = {invalid}")