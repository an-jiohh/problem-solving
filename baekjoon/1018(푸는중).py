#푸는중
x,y = input().split()
x = int(x)
y = int(y)

i = 0
s = []

while i < x :
    s.append(input())
    i += 1

temp = "W"
count1 = 0
for j in s :
    if y % 2 == 0 :
        if temp == "W" : temp = "B"
        else : temp = "W"
    for k in j :
        if k != temp : 
            count1 += 1
        if temp == "W" : temp = "B"
        else : temp = "W"

temp = "B"
count2 = 0
for j in s :
    if y % 2 == 0 :
        if temp == "W" : temp = "B"
        else : temp = "W"
    for k in j :
        if k != temp : 
            count2 += 1
        if temp == "W" : temp = "B"
        else : temp = "W"

if count2 < count1 : print(count2)
else : print(count1)