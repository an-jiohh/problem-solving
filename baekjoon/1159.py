n = int(input())
S = {}

for i in range(n) :
    m = input()
    if m[0] in S :  S[m[0]] = 1
    else : S[m[0]] = S[m[0]] + 1

print(S)