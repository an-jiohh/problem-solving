L = int(input())
S = []
S = input().split()
n = int(input())
sn = 0
ln = 0
for i in S :
    i = int(i)
    if i < n :
        if sn > i : sn = i
    elif i > n :
        if ln < i : ln = i
    elif i == n :
        break
