small_treats = float(input())
medium_treats = float(input())
large_treats = float(input())

happiness_score = 1 * small_treats + 2 * medium_treats + 3 * large_treats

if happiness_score >= 10:
  print("happy")
else:
  print("sad")