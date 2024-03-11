speedlimit = int(input())
speed = int(input())
if (speedlimit >= speed):
    print("Congratulations, you are within the speed limit!")
else:
    if (speed > speedlimit and speed <= speedlimit + 20):
        print("You are speeding and your fine is $100.")
    elif (speed > speedlimit and speed <= speedlimit + 30):
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")