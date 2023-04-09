num = int(input())
sum = 0
for i in str(num):
 sum += int(i)
print("Sum is",sum)

if sum%3 == 0:
 print(True)
else:
 print(False)