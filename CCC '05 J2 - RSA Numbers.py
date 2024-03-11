number_1 = int(input())
number_2 = int(input())
counter = 0
for i in range(number_1, number_2 + 1):
    divisors = 0
    for j in range(1, 1001):
        if i % j == 0:
            divisors += 1
    if divisors == 4:
        counter += 1


print(f"The number of RSA numbers between {number_1} and {number_2} is {counter}")