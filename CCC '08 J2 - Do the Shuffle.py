song_list = ["A", "B", "C", "D", "E"]
while True:
    b = int(input())
    n = int(input())
    if b == 4 and n == 1:
        break
    elif b == 1:
        for i in range(n):
            song = song_list.pop(0)
            song_list.append(song)       
    elif b == 2:
        for i in range(n):
            song =  song_list.pop(-1)
            song_list.insert(0, song)
    elif b == 3:
        for i in range(n):
            song_list[0], song_list[1] = song_list[1], song_list[0]
for i in song_list:
    print(i, end = " ")