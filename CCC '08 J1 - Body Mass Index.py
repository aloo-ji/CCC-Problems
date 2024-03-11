kg = float(input())
m = float(input())
BMI = kg / (m * m)
if BMI < 18.5:
    print("Underweight")
else:
    if (BMI >= 18.5) and (BMI <= 25):
        print("Normal weight")
    else:
        print("Overweight")