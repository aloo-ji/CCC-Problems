Burger = int(input())
Side = int(input())
Drink = int(input())
Dessert = int(input())

Calories = 0

if Burger == 1:
    Calories += 461
else:
    if Burger == 2:
        Calories += 431
    elif Burger == 3:
        Calories += 420
    
if Side == 1:
    Calories += 100
else:
    if Side == 2:
        Calories += 57
    elif Side == 3:
        Calories += 70

if Drink == 1:
    Calories += 130
else:
    if Drink == 2:
        Calories += 160
    elif Drink == 3:
        Calories += 118

if Dessert == 1:
    Calories += 167
else:
    if Dessert == 2:
        Calories += 266
    elif Dessert == 3:
        Calories += 75

print(f"Your total Calorie count is {Calories}.")
