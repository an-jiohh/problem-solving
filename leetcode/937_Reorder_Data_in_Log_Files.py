logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
letter, digit = [], []
for i in logs :
    if i.split()[1].isdigit() :
        digit.append(i)
    else :
        letter.append(i)
    
letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letter + digit)    