alp = input()
alp = list(alp.upper())
set_alp = set(alp)
alp_count = {}
for i in set_alp :
    alp_count[i] = 0

for i in alp :
    alp_count[i] += 1
temp = max(alp_count.values())
check = 0
max_alp = ""
for i in alp_count :
    if alp_count[i] == temp : 
        check += 1
        max_alp = i

if check > 1 : print("?")
else : print(max_alp)