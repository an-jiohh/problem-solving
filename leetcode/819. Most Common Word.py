import collections


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = paragraph.lower()
paragraph = paragraph.split()

a = collections.defaultdict(int)
temp = ""
for i in paragraph :
    temp = ""
    for j in i:
        if(j.isalpha()) : temp = temp + j
    a[temp] += 1
while True :
    temp = max(a, key = a.get)
    if banned.count(temp) == 0 :
        return temp
        break
    else : del(a[temp])