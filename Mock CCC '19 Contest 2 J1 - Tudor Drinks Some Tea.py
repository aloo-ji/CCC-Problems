pearls = 0
for i in range(5):
    straw = input()
    if straw == "P":
        pearls += 1
    else:
        continue
print(pearls)