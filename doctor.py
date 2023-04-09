class Doctor:
 def __init__(self,doctorId,doctorName,specialization,consultationFee):
  self.doctorId = doctorId
  self.doctorName = doctorName
  self.specialization = specialization
  self.consultationFee = consultationFee

class Hospital:
 def __init__(self,doctorDB):
  self.doctorDB = doctorDB
 
 def searchByDoctorName(self,doctorName1):
  lst = []
  for k,v in self.doctorDB.items():
   if v.doctorName.lower() == doctorName1.lower():
    lst.append(v)
  
  if lst == []:
   print("No doctor exists with given name")
  else:
   for i in lst:
    print(i.doctorId)
    print(i.doctorName)
    print(i.specialization)
    print(i.consultationFee)

 def calculateConsultationFee(self,specialization1):
  fee = 0
  for k,v in self.doctorDB.items():
   if v.specialization.lower() == specialization1.lower():
    fee += v.consultationFee
  if fee == 0:
   print("No doctor found")
  else:
   print(fee)

n = int(input())
doctorDB = {}
sno = 1
for i in range(n):
 doctorId = int(input())
 doctorName = input()
 specialization = input()
 consultationFee = int(input())
 doctorDB[sno] = Doctor(doctorId,doctorName,specialization,consultationFee)
 sno+=1

doctorName1 = input()
specialization1 = input()

obj = Hospital(doctorDB)
obj.searchByDoctorName(doctorName1)
obj.calculateConsultationFee(specialization1)




   