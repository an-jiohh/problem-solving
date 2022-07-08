N = int(input())
arr = []
for i in range(N) :
    arr.append(list(input()))
max = 0
me = 0
for i in arr :
    counter = [0 for c in range(N)]
    for n, j in enumerate(i) :
        if j == "Y" :
            counter[n] = 1
            for m, k in enumerate(arr[n]) :
                if k == "Y" :
                    if m != me :
                        counter[m] = 1
    temp = 0
    for j in counter :
        temp += j
    if max < temp : max = temp
    me += 1

print(max)