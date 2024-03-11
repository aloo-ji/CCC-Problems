length_and_speed = input().split()
length_of_path = int(length_and_speed[0])
speed = int(length_and_speed[1])
path = input()

walking_needed = 0

for i in path:
    if i == "U":
        if speed == 0:
            walking_needed += 1
            continue
        speed -= 1
        if speed == 0:
            walking_needed += 1  
    elif i == "D":
        speed += 1
    elif i == "F" and speed == 0:
        walking_needed += 1

print(walking_needed)

