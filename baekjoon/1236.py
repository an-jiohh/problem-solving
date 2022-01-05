# 빈 열, 행을 조사하여 더 많은 경비원이 필요한 열 또는 행의 개수를 출력
y, x = map(int, input().split())

S = []

for i in range(y) :
    S.append(input())

count = 0
ycount = []
for i in range(y) :
    temp = 0
    for j in range(x) :
        if S[i][j] == "X" :
            break
        elif S[i][j] == "." :
            temp += 1
    if temp == x :
        ycount.append(i)

xcount = []
for i in range(x) :
    temp = 0
    for j in range(y) :
        if S[j][i] == "X" :
            break
        elif S[j][i] == "." :
            temp += 1
    if temp == y :
        xcount.append(i) 

if len(xcount) >= len(ycount) :
    print(len(xcount))
else :
    print(len(ycount))