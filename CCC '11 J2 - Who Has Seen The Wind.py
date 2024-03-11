h = int(input())
M = int(input())
for t in range(1, M+1):
    A = (-6 * t**4) + (h * t**3) + (2 * t**2) + t
    if A <= 0 or t == M:
        break
if t >= M:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon first touches ground at hour:")
    print(t)