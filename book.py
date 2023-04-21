class Book:
 def __init__(self,pages,price,author,id,title):
  self.pages = pages
  self.price = price
  self.author = author
  self.id = id
  self.title = title

class BookStore:
 def __init__(self,store_name, book_lst):
  self.store_name = store_name
  self.book_lst = book_lst
 
 def findMinimumBookByid(self):
  lst = []
  for i in self.book_lst:
   lst.append(i.id)
  
  if lst == []:
   print("Not Found")
  else:
   for j in self.book_lst:
    if j.id == min(lst):
     print(j.pages)
     print(j.price)
     print(j.author)
     print(j.id)
     print(j.title)

 def sortBookByid(self):
  lst1 = []
  for i in self.book_lst:
   lst1.append(i.id)
  
  if lst1 == []:
   print("None")
  else:
   lst1.sort()
   for i in lst1:
    print(i)

n = int(input())
book_lst = []
for i in range(n):
 pages = int(input())
 price = int(input())
 author = input()
 id = int(input())
 title = input()
 book_lst.append(Book(pages,price,author,id,title))

res = BookStore("ABC",book_lst)
res.findMinimumBookByid()
res.sortBookByid()


 