numbers = input().split()

N = int(numbers[0])

A = int(numbers[1])
B = int(numbers[2])

andrew_time = 0
tommy_time = 0

for _ in range(N):
    obstacle_heights = input().split()
    if int(obstacle_heights[0]) >= A:
        andrew_time += 2
    elif int(obstacle_heights[0]) < A:
        andrew_time += 1
    if int(obstacle_heights[1]) >= B:
        tommy_time += 2
    elif int(obstacle_heights[1]) < B:
        tommy_time += 1

if andrew_time == tommy_time:
    print("Tie!")
elif andrew_time < tommy_time:
    print("Andrew wins!")
else:
    print("Tommy wins!")