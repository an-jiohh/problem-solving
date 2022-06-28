N, T, P = map(int, input().split())
score = []
if N != 0 :
    score = list(map(int, input().split()))
    score.append(T)
    score.sort(reverse=True)
    lanking = score.index(T) + 1
    if lanking > P : lanking = -1
    else :
        if N == P and score[-1] == T:
            lanking = -1

else : lanking = 1
print(lanking)