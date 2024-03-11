phone_number = input()

list_of_phone_number = phone_number.split() 

if len(phone_number) == 11:
    if list_of_phone_number[0] == "416":
        print("valuable")
    elif list_of_phone_number[0] == "647" or list_of_phone_number[0] == "437":
        print("valueless")
    else:
        print("invalid")
else:
    print("invalid")