S = []
i = 0
while i < 8 :
    S.append(input())
    i += 1

check = 1
count = 0
for j in S :
    for k in j :
        if (k == "F") & (check == 1) : 
            count += 1
        check = check * -1
    check = check * -1

print(count)