sum = 0
N = int(input())
for i in range(N):
    number = int(input())
    if number % 10 == 0:
        continue
    else:
        sum += number
print(sum)