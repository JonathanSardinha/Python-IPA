str = input("Enter a string")
suffix = 'ly'
str = str.split()
str1 = ""
for i in str:
 if i.endswith(suffix):
  i = i.removesuffix(suffix)
  str1 = str1 + " " + i
 else:
  str1 = str1 + " " + i

print(str1)