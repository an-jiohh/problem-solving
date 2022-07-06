n = int(input())
ball = [1,0,0]
def change(x, y) :
    temp = ball[x - 1]
    ball[x - 1] = ball[y - 1]
    ball[y - 1] = temp

for i in range(n) :
    x, y = map(int, input().split())
    change(x, y)

for i in range(3) :
    if ball[i] : print(i+1)