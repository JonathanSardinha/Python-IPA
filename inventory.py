class Inventory:
 def __init__(self,inventoryId,max_quantity,current_quantity,threshold):
  self.inventoryId = inventoryId
  self.max_quantity = max_quantity
  self.current_quantity = current_quantity
  self.threshold = threshold

class Solution:
 @staticmethod
 def replenish(lst_inventory,threshold1):
  lst = []
  for i in lst_inventory:
   if i.threshold <= threshold1:
    lst.append(i)
  
  if lst == []:
   print("Not Found")
  else:
   for j in lst:
    if j.threshold >= 75:
     print(j.inventoryId, "Critical Filling")
    elif 50 <= j.threshold <= 74:
     print(j.inventoryId, "Moderate Filling")
    else:
     print(j.inventoryId,"Non-Critical Filling")
 

n = 4
lst_inventory = []
for i in range(n):
 inventoryId = input()
 max_quantity = int(input())
 current_quantity = int(input())
 threshold = int(input())
 lst_inventory.append(Inventory(inventoryId,max_quantity,current_quantity,threshold))

threshold1 = int(input())

res = Solution()
res.replenish(lst_inventory,threshold1)