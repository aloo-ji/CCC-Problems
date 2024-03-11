N = int(input())
N += 1
N = str(N)
while "0" in N:
    N = int(N)
    N += 1
    N = str(N)
print(N)

# nicer way of doing it

N = int(input()) + 1
while "0" in str(N):
    N += 1
print(N)