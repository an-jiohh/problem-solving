n = int(input())
slist = []
for i in range(n) :
    slist.append(input())

list = list(set(slist))
list.sort()
list.sort(key=lambda i:len(i))
for i in list:
    print(i)

