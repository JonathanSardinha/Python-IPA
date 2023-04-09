class Bill:
 def __init__(self,billNo,name,connection_type,billAmount,status):
  self.billNo = billNo
  self.name = name
  self.connection_type = connection_type
  self.billAmount = billAmount
  self.status = status

class Solution:
 @staticmethod
 def findBillWithMaxAmount(bill_lst,inpt_status):
  lst = []
  for i in bill_lst:
   if i.status.lower() == inpt_status.lower():
    bill_lst.sort(key = lambda x:x.billNo)
    lst.append(i)

  if lst == []:
   print("None")
  else:
   for i in lst:
    lst.sort(key = lambda x:x.billAmount, reverse = True)
    print(i.billNo,i.name,sep = "#")
    break
    

 @staticmethod
 def getCountWithTypeOfConnection(bill_lst,inpt_connectionType):
  count = 0
  for i in bill_lst:
   if i.connection_type.lower() == inpt_connectionType.lower():
    count += 1
  if count == 0:
   print("None")
  else:
   print(count)

 

n = int(input())
bill_lst = []
for i in range(n):
 billNo =  int(input())
 name = input()
 connection_type = input()
 billAmount = float(input())
 status = input()
 bill_lst.append(Bill(billNo,name,connection_type,billAmount,status))

inpt_status = input()
inpt_connectionType = input()

Solution.findBillWithMaxAmount(bill_lst,inpt_status)
Solution.getCountWithTypeOfConnection(bill_lst,inpt_connectionType)

