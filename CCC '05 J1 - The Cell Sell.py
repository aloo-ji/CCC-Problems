
daytime = int(input())
evening = int(input())
weekend = int(input())
if daytime < 100:
    plan_a_cost = evening * 0.15 + weekend * 0.20
else:
    plan_a_cost = (daytime - 100) * 0.25 + evening * 0.15 + weekend * 0.2
if daytime < 250:
    plan_b_cost = evening * 0.35 + weekend * 0.25
else:
    plan_b_cost = (daytime - 250) * 0.45 + evening * 0.35 + weekend * 0.25

print("Plan A costs %.2f" % plan_a_cost)
print(f"Plan B costs %.2f" % plan_b_cost)

if plan_a_cost > plan_b_cost:
    print("Plan B is cheapest.")
elif plan_b_cost > plan_a_cost:
    print("Plan A is cheapest.")
else:
    print("Plan A and B are the same price.")