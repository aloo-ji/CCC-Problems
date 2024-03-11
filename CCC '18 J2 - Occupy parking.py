N = int(input())
parking_1 = input()
parking_2 = input()
counter = 0
for i in range(N):
    if parking_1[i] == parking_2[i] and parking_1[i] == "C":
        counter += 1

print(counter)