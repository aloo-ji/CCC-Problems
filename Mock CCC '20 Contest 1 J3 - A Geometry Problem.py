X = int(input())
Y = int(input())
answer = X * Y // 4

if X * Y % 4 == 0:
    decimal = ".00"
if X * Y % 4 == 1:
    decimal = ".25"
if X * Y % 4 == 2:
    decimal = ".50"
if X * Y % 4 == 3:
    decimal = ".75"
print(str(answer) + decimal)