n, w, l = map(int, input().split())

li = list(map(int, input().split()))

w_max = 0
counter = 1
brige = []
truck = 0

while len(li) != 0 or len(brige) != 0:
    counter += 1
    if len(li) > truck :
        if w_max + li[truck] <= l :
            w_max += li[truck]
            truck += 1
            brige.append(w)
    for i in range(len(brige)) :
        brige[i] = brige[i] - 1
    if brige[0] == 0 : 
        w_max -= li.pop(0)
        truck -= 1
        brige.pop(0)

print(counter)