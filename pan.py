class Pan:
 def __init__(self,id,material,brand,price,capacity):
  self.id = id
  self.material = material
  self.brand = brand
  self.price = price
  self.capacity = capacity

class Solution:
 @staticmethod
 def costliestPan(lst_pan,material1):
  lst_cost = []
  for i in lst_pan:
   if i.material.lower() == material1.lower():
    lst_cost.append(i.price)
  
  if lst_cost == []:
   print("No pan with the given material")
  else:
   for j in lst_pan:
    if j.price == max(lst_cost):
     print(j.id)

 @staticmethod
 def discountedPrice(lst_pan,brand1):
  for i in lst_pan:
   if i.brand.lower() == brand1.lower():
    if 1000> i.capacity > 500:
     i.price -= (i.price * (20/100))
     print(int(i.price))
    
    if i.capacity>1000:
     i.price -= (i.price*(26/100))
     print(int(i.price))


n = int(input())
lst_pan = []
for i in range(n):
 id = input()
 material = input()
 brand = input()
 price = int(input())
 capacity = int(input())
 lst_pan.append(Pan(id,material,brand,price,capacity))

material1 = input()
brand1 = input()
Solution.costliestPan(lst_pan,material1)
Solution.discountedPrice(lst_pan,brand1)