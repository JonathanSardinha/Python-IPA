class Vegetable:
 def __init__(self,name,price,quantity):
  self.name = name
  self.price = price
  self.quantity = quantity

class Store:
 def __init__(self,storeName,lst_veg):
  self.storeName = storeName
  self.lst_veg = lst_veg

 def categorizeVegetablesAlphabetically(self):
  self.lst_veg = sorted(self.lst_veg, key=lambda x:x.name)
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  dict = {}

  for char in alphabets:
   lst = []
   for i in self.lst_veg:
    if char.lower() == i.name[0].lower():
     lst.append(i.name)
   
   if len(lst)>0:
    dict[char] = tuple(lst)
  
  return dict

 def filterVegetablesForPriceRange(self,min_price,max_price):
  lst_price = []
  for i in self.lst_veg:
   if min_price <= i.price <= max_price:
    lst_price.append(i.name)
  
  if len(lst_price) == 0:
   return None
  else:
   lst_price.sort()
   return lst_price


n = int(input())
lst_veg = []
for i in range(n):
 name = input()
 price = float(input())
 quantity = int(input())
 lst_veg.append(Vegetable(name,price,quantity))

storeName = input()
min_price = float(input())
max_price = float(input())



store = Store(storeName, lst_veg)
res1 = store.categorizeVegetablesAlphabetically()
if res1 == {}:
 print("No Vegetables")
else:
 for k,v in res1.items():
  print(k)
  for j in v:
   print(j)
  

res2 = store.filterVegetablesForPriceRange(min_price,max_price)
if res2 == []:
 print("No vegetables found in the given price range")
else:
 print(f'{min_price}-{max_price}')
 for i in res2:
  print(i)