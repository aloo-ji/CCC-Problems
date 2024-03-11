V = int(input())
votes = input()
A_votes = 0
B_votes = 0
for i in votes:
    if i == "A":
        A_votes += 1
    else:
        B_votes += 1
if A_votes > B_votes:
  print("A")
elif A_votes < B_votes:
  print("B")
else:
  print("Tie")

# V = int(input())
# votes = input()

# A_votes = votes.count("A")
# B_votes = votes.count("B")

# if A_votes > B_votes:
#   print("A")
# elif A_votes < B_votes:
#   print("B")
# else:
#   print("Tie")