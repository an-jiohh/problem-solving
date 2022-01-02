L = int(input())
S = []
S = input().split()
n = int(input())
sn = 0
ln = 1001
for i in S :
    i = int(i)
    if i < n :
        if sn < i : sn = i
    elif i > n :
        if ln > i : ln = i
    elif i == n :
        ln = -1
        break

count = 0
if ln == -1 : print(count)
else :
    while True :
        sn += 1
        if sn != n :
            count += ln - n
        elif sn == n :
            count += ln - n - 1 #[sn,n][2,2]은 경우를 없애기 위해 1을 빼준다.
            break
    print(count)