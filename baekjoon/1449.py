N, L = map(int, input().split())
S = []
S = input().split()
i = 0
while i < N:
    S[i] = int(S[i])
    i += 1
S.sort()
L = L - 1 #양옆으로 0.5가 필요하므로 왼쪽 0.5 + 오른쪽 0.5하여 1을 뺴줌

i = 0
count = 0
while i < N:
    temp = S[i] + L
    i += 1
    while i < N:
        if (S[i] <= temp): i += 1
        else :
            count += 1 
            break
    if i == N :
        count += 1

print(count)