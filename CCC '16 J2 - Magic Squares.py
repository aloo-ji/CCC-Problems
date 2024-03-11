row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
row_4 = input().split()
if int(row_1[0]) + int(row_1[1]) + int(row_1[2]) + int(row_1[3]) == int(row_2[0]) + int(row_2[1]) + int(row_2[2]) + int(row_2[3]) == int(row_3[0]) + int(row_3[1]) + int(row_3[2]) + int(row_3[3]) == int(row_4[0]) + int(row_4[1]) + int(row_4[2]) + int(row_4[3]):
    if int(row_1[0]) + int(row_2[0]) + int(row_3[0]) + int(row_4[0]) == int(row_1[1]) + int(row_2[1]) + int(row_3[1]) + int(row_4[1]) == int(row_1[2]) + int(row_2[2]) + int(row_3[2]) + int(row_4[2]) == int(row_1[3]) + int(row_2[3]) + int(row_3[3]) + int(row_4[3]):
        print("magic")
    else:
        print("not magic")
else:
    print("not magic")