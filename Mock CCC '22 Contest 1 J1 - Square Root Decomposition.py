N = int(input())
i = int(input()) 
j = int(input())

if abs(N - i ** 2) <= abs(N - j ** 2):
    print(1)
else:
    print(2)