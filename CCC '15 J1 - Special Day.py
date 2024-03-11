month = int(input())
day = int(input())

if month == 1:
    print("Before")

if month > 2:
    print("After")

if (month == 2) and (day < 18):
    print("Before")
else:
    if (month == 2) and (day > 18):
        print("After")
    elif (month == 2) and (day == 18):
        print("Special")