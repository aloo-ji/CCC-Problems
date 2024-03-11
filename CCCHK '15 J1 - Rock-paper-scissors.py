N = int(input())
alice_sequence = input().split()
bob_sequence = input().split()

alice_wins = 0
bob_wins = 0

for i in range(0, N):
    alice_move = alice_sequence[i]
    bob_move = bob_sequence[i]
    if (alice_move == "rock" and bob_move == "scissors") or (alice_move == "paper" and bob_move == "rock") or (alice_move == "scissors" and bob_move == "paper"):
        alice_wins += 1
    elif (bob_move == "rock" and alice_move == "scissors") or (bob_move == "paper" and alice_move == "rock") or (bob_move == "scissors" and alice_move == "paper"):
        bob_wins += 1
print(alice_wins, bob_wins)