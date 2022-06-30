ty, tw, td = map(int, input().split())
dy, dw, dd = map(int, input().split())

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def check(year) :
    if year % 400 == 0 : return 1
    elif year % 100 == 0 : return 0
    elif year % 4 == 0 : return 1
    return 0
start = td
for i in range(ty) :
    start += 365 + check(i)
for i in range(tw) :
    if i != 2 : start += day[i]
    else : start += day[i] + check(ty)

end = dd
for i in range(dy) :
    end += 365 + check(i)
for i in range(dw) :
    if i != 2 : end += day[i]
    else : end += day[i] + check(dy)

if dy - ty == 1000 and (tw <= dw and td <= dd) : print("gg")
elif dy - ty > 1000 : print("gg")
else : print("D-{}".format(end-start))