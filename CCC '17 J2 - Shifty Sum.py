N = int(input())
k = int(input())
sum = 0
for i in range(0, k+1):
    sum += N*10**i
print(sum)