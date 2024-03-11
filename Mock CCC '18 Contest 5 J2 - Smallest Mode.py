from statistics import mode

N = int(input())
numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
print(mode(numbers))