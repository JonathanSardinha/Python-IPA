def str_num_list(string):
 alpha = ""
 num = ""
 for char in string:
  if char.isalpha():
   alpha += char
  if char.isdigit():
   num += char
 
 lst = []
 if len(alpha)>0:
  lst.insert(0,alpha)
 if len(num)>0:
  lst.insert(1,int(num))

 return lst

string = input()
res = str_num_list(string)
print(res)