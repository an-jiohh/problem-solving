N = int(input())

for i in range(N, 3, -1) :
    check = 0
    for j in str(i) :
        if j != "7" and j != "4" :
            check = 1
            break 
    if check == 0 : 
        print(i)
        break