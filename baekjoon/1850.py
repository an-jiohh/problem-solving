a, b = map(int, input().split())
if a < b : a, b = b, a
n = 1
while b :
    n = a % b
    a = b
    b = n

for i in range(a):
    print("1", end="")