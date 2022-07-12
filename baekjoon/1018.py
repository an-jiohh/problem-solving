y, x = map(int, input().split())

arr = []
check_startW = [["W","B"] * 4 for i in range(8)]
check_startB = [["B","W"] * 4 for i in range(8)]

for i in range(1, 8, 2) :
    check_startW[i], check_startB[i] = check_startB[i], check_startW[i]

for i in range(y) :
    arr.append(list(input()))

def check(iny, inx) :
    checkW = 0
    checkB = 0
    for i in range(8) :
        for j in range(8) :
            if arr[iny + i][inx + j] != check_startW[i][j] : checkW += 1
            if arr[iny + i][inx + j] != check_startB[i][j] : checkB += 1
    if checkW >= checkB : return checkB
    else : return checkW

min = 65
for i in range(y - 7) :
    for j in range(x - 7) :
        temp = check(i, j)
        if temp < min : min = temp

print(min)