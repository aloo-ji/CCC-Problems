counter = 0
for i in range(6):
    letter = input()
    if letter == "W":
        counter += 1
if counter == 0:
    print(-1)
else:
    if (counter == 1) or (counter == 2):
        print(3)
    elif (counter == 3) or (counter == 4):
        print(2)
    else:
        print(1)
