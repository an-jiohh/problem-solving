n = int(input())
a = input().split()
b = input().split()

for i in range(n) :
    a[i] = int(a[i])
    b[i] = int(b[i])
a.sort()
b.sort()
b.reverse()
count = 0
for i in range(n):
    count += a[i] * b[i]
print(count)