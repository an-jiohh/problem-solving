n, x = map(int, input().split())

list = [i for i in range(1, n+1)]
t = x - 1
x = x - 1
print("<",end="")
for i in range(n) :
    print(f"{list.pop(t)}", end="")
    n -= 1
    if n != 0 : 
        t = (t + x) % n 
        print(", ", end="")
print(">")