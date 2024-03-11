C = int(input())
casper_best_fish = 0

for i in range(C):
    fish = input().split()
    worth_of_fish = int(fish[0]) * int(fish[1])
    if worth_of_fish > casper_best_fish:
        casper_best_fish = worth_of_fish

N = int(input())
natalie_best_fish = 0

for i in range(N):
    fish = input().split()
    worth_of_fish = int(fish[0]) * int(fish[1])
    if worth_of_fish > natalie_best_fish:
        natalie_best_fish = worth_of_fish

if casper_best_fish > natalie_best_fish:
    print("Casper")
elif natalie_best_fish > casper_best_fish:
    print("Natalie")
else:
    print("Tie")