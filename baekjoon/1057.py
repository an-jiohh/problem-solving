import math
n, x, y = map(int, input().split())
counter = 1
x, y = x - 1, y - 1
while n >= 2 :
    if x // 2 == y // 2 :
        print(counter)
        break
    counter += 1
    x, y = x // 2, y // 2
    n = math.ceil(n / 2)