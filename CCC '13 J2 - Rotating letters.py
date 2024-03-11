counter = 0
n = input()
counter += n.count("I")
counter += n.count("O")
counter += n.count("S")
counter += n.count("H")
counter += n.count("Z")
counter += n.count("X")
counter += n.count("N")

if counter == len(n):
  print("YES")
else:
  print("NO")