

a=input().upper()

b=list(set(a))

max:str = 0
max_cha:int = ""
for i in b:
    temp = a.count(i)
    if max == temp : 
        max_char = "?"
    elif max < temp : 
        max_char = i
        max = temp

print(max_char)