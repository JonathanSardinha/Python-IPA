class Laptop:
 def __init__(self,laptopId,brand,osType,price,rating):
  self.laptopId = laptopId
  self.brand = brand
  self.os = os
  self.price = price
  self.rating = rating

class Solution:
 @staticmethod
 def countOfLaptopsByBrand(lst_laptop,brand1):
  count = 0
  for i in lst_laptop:
   if i.brand.lower() == brand1.lower() and i.rating > 3:
    count += 1

  if count == 0:
   print("Given brand is not available")
  else:  
   print(count)

 @staticmethod
 def searchLaptopByOsType(lst_laptop,os1):
  lst = []
  for i in lst_laptop:
   if i.os.lower() == os1.lower():
    lst.append(i)
  
  if lst == []:
   print("Given OS not available")
  else:
   lst.sort(key = lambda x:x.laptopId, reverse = True)
   for j in lst:
    print(j.laptopId)
    print(j.rating)

n = 4
lst_laptop = []
for i in range(n):
 laptopId = int(input())
 brand = input()
 os = input()
 price = float(input())
 rating = int(input())
 lst_laptop.append(Laptop(laptopId,brand,os,price,rating))

brand1 = input()
os1 = input()

Solution.countOfLaptopsByBrand(lst_laptop,brand1)
Solution.searchLaptopByOsType(lst_laptop,os1)
