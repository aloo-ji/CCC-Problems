P = int(input())
Q = int(input())
W = int(input())
term_mark = 1 - W/100
W = W/100

def normal_round(number):
    return int(number + 0.5)

for i in range(0,101):
    if normal_round(P * term_mark + W * i) >= Q:
        print(i)
        break
else:
    print("DROP THE COURSE")

