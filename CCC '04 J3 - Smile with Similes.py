n = int(input())
m = int(input())
adjective_list = []
noun_list = []
for i in range(n):
    adjective = input()
    adjective_list.append(adjective)
for i in range(m):
    noun = input()
    noun_list.append(noun)

for adjective in adjective_list:
    for noun in noun_list:
        print(f"{adjective} as {noun}")