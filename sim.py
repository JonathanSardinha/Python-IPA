class Sim:
 def __init__(self,simId,customerName,balance,rate,circle):
  self.simId = simId
  self.customerName = customerName
  self.balance = balance
  self.rate = rate
  self.circle = circle

class Solution:
 @staticmethod
 def transferCustomerCircle(lst_sim,circle1,circle2):
  lst = []
  for i in lst_sim:
   if i.circle.lower() == circle1.lower():
    i.circle = circle2
    lst.append(i)
  if lst == []:
   print("Not Found")
  else:
   lst.sort(key=lambda x:x.rate, reverse = True)
   for j in lst:
    print(j.simId,j.customerName,j.circle,j.rate)

n = int(input())
lst_sim = []
for i in range(n):
 simId = int(input())
 customerName = input()
 balance = float(input())
 rate = float(input())
 circle = input()
 lst_sim.append(Sim(simId,customerName,balance,rate,circle))

circle1 = input()
circle2 = input()

Solution.transferCustomerCircle(lst_sim,circle1,circle2)



