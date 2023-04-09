class Employee:
 def __init__(self,emp_name,designation,salary,overtime,overtime_status = False):
  self.emp_name = emp_name
  self.designation = designation
  self.salary = salary
  self.overtime = overtime
  self.overtime_status = overtime_status

class Organization:
 def __init__(self,employee_lst):
  self.employee_lst = employee_lst

 def checkforBonus(self,overtime_threshold):
  for i in self.employee_lst:
   if not sum(i.overtime.values()) < overtime_threshold:
    i.overtime_status = True
   else:
    i.overtime_status = False
    print(i.emp_name, i.overtime_status)

 def calculateBonus(self,rate_perhour):
  bonus = []
  for i in self.employee_lst:
   if i.overtime_status == True:
    bonus.append(sum(i.overtime.values()) * rate_perhour)
  print (sum(bonus))
    

n = int(input())
employee_lst = []
for i in range(n):
 emp_name = input()
 designation = input()
 salary = int(input())
 otc = {}
 n1 = int(input())
 for i in range(n1):
  month = input()
  over_time = int(input())
  otc[month] = over_time
 employee_lst.append(Employee(emp_name,designation,salary,otc))

overtime_threshold = int(input())
rate_perhour = int(input())

org = Organization(employee_lst)
org.checkforBonus(overtime_threshold)
org.calculateBonus(rate_perhour)
