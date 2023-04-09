string = input()
characters = 0
spaces = 0

for char in string:
 if char.isalpha():
  characters += 1
 elif char.isspace():
  spaces +=1
 elif char.isdigit():
  continue


print(f'No of spaces : {spaces} \nand characters: {characters}')