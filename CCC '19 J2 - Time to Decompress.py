N = int(input())

for i in range(N):
    number_and_symbol = input().split()
    number = int(number_and_symbol[0])
    symbol = number_and_symbol[1]
    print(symbol * number)
