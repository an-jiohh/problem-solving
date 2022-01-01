n = int(input())
i = 0
sub = []
while i < n :
    sub.append(input())
    i += 1

count = 1
while True :
    checksub = []
    for j in sub :
        checksub.append(j[-count:])
    checksub = set(checksub)
    if(len(checksub) == n) : break
    else : count += 1

print(count)