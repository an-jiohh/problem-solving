import sys

li = []
re = int(input())
n = 0
for i in range(re) :
    a = sys.stdin.readline().split()
    if a[0] == "push" :
        li.append(a[1])
        n += 1
    elif a[0] == "pop" :
        if n != 0 :
            n -= 1
            print(li.pop())
        else :
            print("-1")
    elif a[0] == "size" :
        print(n)
    elif a[0] == "empty" :
       if n == 0 : print("1")
       elif n != 0 : print("0")
    elif a[0] == "top" :
        if n == 0 : print("-1")
        else : print(li[n-1])