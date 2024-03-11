seats = input().split()
F = int(seats[0])
M = int(seats[1])
B = int(seats[2])

tickets = input().split()
F_tickets = int(tickets[0])
M_tickets = int(tickets[1])
B_tickets = int(tickets[2])

number_1 = F_tickets + M_tickets + B_tickets

number_2 = F * F_tickets + M * M_tickets + B * B_tickets

print(number_1, number_2)