class MovieInfo:
 def __init__(self,title,year,awards,nomination,country):
  self.title = title
  self.year = year
  self.awards = awards
  self.nomination = nomination
  self.country = country

class Award:
 def __init__(self,lst_movie):
  self.lst_movie = lst_movie

 def AwardYear(self,cyear):
  if len(self.lst_movie) == 0:
   return None
  else:
   lst = []
   for i in self.lst_movie:
    if i.year == cyear:
     if i.country != 'America':
      lst.append(i)
   return lst

 def AwardDict(self):
  if len(self.lst_movie) == 0:
   return None
  else:
   d = dict()
   for i in self.lst_movie:
    srate = (i.awards/i.nomination)*100
    srate = int(srate)
    d[i.title] = srate
   srted = dict(sorted(d.items(),key = lambda x:x[1], reverse = True))
   return srted


n = int(input())
mlist = []
for i in range(n):
 title = input()
 year=int(input())
 awards = int(input())
 nomination = int(input())
 country = input()
 mlist.append(MovieInfo(title,year,awards,nomination,country))

obj = Award(mlist)
Awardyear = int(input())
res1 = obj.AwardYear(Awardyear)
if res1:
 for i in res1:
  print(i.title)
  print(i.year)
  print(i.awards)
  print(i.nomination)
  print(i.country)
else:
 print("No Movie Found")


res2 = obj.AwardDict()
if res2:
 for k,v in res2.items():
  print(k,v)
else:
 print("Unable to create dictionary")


