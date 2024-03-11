players = int(input())
gold = 0 
goldrating = ""

for i in range(players):
  scores = int(input())
  fouls = int(input())
  pts = (5*scores) - (3*fouls)
  if pts > 40:
    gold += 1

if gold == players:
  goldrating = "+"

print(str(gold) + goldrating)