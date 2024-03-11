

txt_diction = {'CU': 'see you', ':-)': "I'm happy", ':-(': "I'm unhappy", ';-)': 'wink', ':-p': 'stick out my tongue', '(~.~)': 'sleepy', 'TA': 'totally awesome', 'CCC': 'Canadian Computing Competition', 'CUZ': 'because', 'TY': 'thank-you', "YW": "you're welcome", 'TTYL': 'talk to you later'}
    
while True:
    short_form = input()
    if short_form == "TTYL":
        print("talk to you later")
        break
    if short_form in txt_diction:
        print(txt_diction[short_form])
    else:
        print(short_form)

