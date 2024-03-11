A3Pointers = int(input())
A2Pointers = int(input())
A1Pointers = int(input())
B3Pointers = int(input())
B2Pointers = int(input())
B1Pointers = int(input())

A_Score = (A3Pointers * 3) + (A2Pointers * 2) + (A1Pointers)
B_Score = (B3Pointers * 3) + (B2Pointers * 2) + (B1Pointers)

if (A_Score > B_Score):
    print("A")
elif (B_Score > A_Score):
    print("B")
else:
    print("T")
