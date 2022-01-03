def func(num) :
    counter = num
    for i in range(4,-1,-1) :
        counter += int(num / (10 ** i))
        num = num % (10 ** i)
    return counter

j = 1
S = []
while j <= 10000 :
    S.append(func(j))
    j += 1

j = 1
while j <= 10000 :
    if S.count(j) == 0 : print(j)
    j += 1