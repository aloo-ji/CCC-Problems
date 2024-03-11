N = int(input())
Rating = 0
peppers = {"Poblano": 1500,
"Mirasol": 6000,
"Serrano": 15500,
"Cayenne": 40000,
"Thai": 75000,
"Habanero": 125000}

for i in range(N):
    pepper = input()
    Rating += peppers[pepper]

print(Rating)