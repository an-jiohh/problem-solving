def solution(s):
    min = len(s)
    for i in range(1,int(len(s)/2) + 1) : 
        temp = s
        check = 0
        ch = s[0:0+i] #슬라이딩 윈도우
        sum = 0
        for j in range(i, len(s), i) :
            if ch == s[j : j+i] :
                if check == 0 : sum += 1
                temp = temp.replace(ch, "", 1)
                check += 1
                if check == 9 : sum += 1
            else : check = 0
            ch = s[j : j+i] ## 다음슬라이드로 변경
        if min >= len(temp) + sum : min = len(temp) + sum
    return min

t = "xxxxxxxxxxyyy"
print(solution(t))