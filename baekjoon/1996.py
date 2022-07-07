n = int(input())

m = []
for i in range(n) :
    m.append(list(input()))
check_map = [[-1,-1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1]]
def check(y, x) :
    counter = 0
    for i in check_map :
        if y + i[0] >= 0 and x + i[1] >= 0 and y + i[0] < n and x + i[1] < n :
            if m[y + i[0]][x + i[1]] != "." :
                counter += int(m[y + i[0]][x + i[1]])
    return counter

for i in range(n) :
    for j in range(n) :
        if m[i][j] != "." : print("*", end="")
        else : 
            if check(i, j) > 9 : print("M", end="")
            else: print(check(i, j),end="")
    print("")