happy = 0
sad = 0
sentence = input()
happy += sentence.count(":-)")
sad += sentence.count(":-(")
if (happy == sad) and (happy == 0):
    print("none")
elif (happy == sad) and (happy != 0):
    print("unsure")
elif (happy > sad):
    print("happy")
else:
    print("sad")