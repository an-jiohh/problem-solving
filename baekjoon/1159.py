n = int(input())
S = {}

for i in range(n) :
    m = input()
    if m[0] in S :  
        S[m[0]] = S[m[0]] + 1
    else : 
        S[m[0]] = 1

count = 0
name = []
for i in S:
    if S[i] >= 5 :
        name.append(i)
        count += 1

if count == 0 :
    print("PREDAJA")
else :
    name.sort()
    for i in name :
        print(i,end="")