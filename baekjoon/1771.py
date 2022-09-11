a=input().upper()

b=list(set(a))

p=[]
for i in b:
    p.append(a.count(i))
    
p.sort()
p=p[::-1]


if len(p)==1:
    print(a[0])
elif len(p)>1 and p[0]==p[1]:
    print('?')
else:
    print(max(a, key=a.count))