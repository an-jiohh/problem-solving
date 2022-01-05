n = int(input())
A = []
A = input().split()
for i in range(n):
    A[i] = int(A[i])
m = int(input())
B = []
B = input().split()
for i in range(n):
    B[i] = int(B[i])

for i in B :
    count = 0
    for j in A:
        if i==j :
            print(1)
            break
        else : count += 1
    if count == m : print(0) 