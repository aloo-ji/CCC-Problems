a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b and b == c and c == d:
    print("Fish At Constant Depth")
elif d > c and c > b and b > a:
    print("Fish Rising")
elif a > b and b > c and c > d:
    print("Fish Diving")
else:
    print("No Fish")