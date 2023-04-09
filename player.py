class Player:
 def __init__(self,playerId,playerName,runs,playerType,matchType):
  self.playerId = playerId
  self.playerName = playerName
  self.runs = runs
  self.playerType = playerType
  self.matchType = matchType

class Solution:
  @staticmethod
  def findPlayerWithLowestRuns(lst_player,playerType1):
   run = []
   for i in lst_player:
    if i.playerType.lower() == playerType1.lower():
     run.append(i.runs)
   if run == []:
    print("No runs Found")
   else:
    print(min(run))
 
  @staticmethod
  def findPlayerByMatchType(lst_player,matchType1):
   lst = []
   for i in lst_player:
    if i.matchType.lower() == matchType1.lower():
     lst.append(i)
   if lst == []:
    print("No data found")
   else:
    lst.sort(key = lambda x:x.playerId, reverse = True) 
    for j in lst:
     print(j.playerId)
   
n = 4
lst_player = []
for i in range(n):
 playerId = int(input())
 playerName = input()
 runs = int(input())
 playerType = input()
 matchType = input()
 lst_player.append(Player(playerId,playerName,runs,playerType,matchType))

playerType1 = input()
matchType1 = input()

Solution.findPlayerWithLowestRuns(lst_player,playerType1)
Solution.findPlayerByMatchType(lst_player,matchType1)

 
  