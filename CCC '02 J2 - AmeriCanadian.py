word = ''
vowels = ["a", "e", "i", "o", "u", "y"]
while True:
    word = input()
    if word == "quit!":
        break
    elif len(word) > 4 and word.endswith("or") and word[-3] not in vowels:
        word = word.replace('or', "our")
        print(word)
    else:
        print(word)