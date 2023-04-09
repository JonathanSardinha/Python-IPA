string = input()
vowels = "aeiouAEIOU"
countVowel = 0
countConsonant = 0

for char in string:
 if char.isalpha() == True:
  if char in vowels:
   countVowel += 1
  elif char not in vowels:
   countConsonant +=1
  else:
   print("Not an alphabet")

print(f'Vowels count - {countVowel}\nConsonants count - {countConsonant}')