previous_letter = ""
coconut_jelly = 0

for i in range(7):
    letter = input()
    if letter == "J":
        if previous_letter == "J":
            continue
        else:
            coconut_jelly += 1
            previous_letter = "J"
    else:
        previous_letter = "T"
print(coconut_jelly)
    
