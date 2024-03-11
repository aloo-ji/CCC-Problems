dusa_size = int(input())
yobis = []
while True:
    try:
        yobi_size = int(input())
        yobis.append(yobi_size)
    except EOFError:
        break

for yobi_size in yobis:
    if yobi_size < dusa_size:
        dusa_size += yobi_size
    else:
        break

print(dusa_size)