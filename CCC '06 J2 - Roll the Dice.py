dice1 = int(input())
dice2 = int(input())

total = 0

for x in range(1, dice1 + 1):
  for y in range(1, dice2 + 1):
    if x+y == 10:
      total += 1
      
if total == 1: 
  print ('There is '+ str(total) + ' way to get the sum 10.')
else:
  print ('There are '+ str(total) + ' ways to get the sum 10.')