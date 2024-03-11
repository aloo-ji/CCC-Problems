def solution_1():
    N = int(input())
    for i in range(N):
        number = input()
        while len(number) != 1:
            counter = 0
            for j in number:
                counter += int(j)
            number = str(counter)
        print(number)

def solution_2():
    def digit_root(n): 
        return (n - 1) % 9 + 1

    N = int(input())
    for i in range(N):
        print(digit_root(int(input())))

solution_1()