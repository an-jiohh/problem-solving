def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    stack = ""
    answer = ""
    for i in s :
        if i.isdigit() == 0 :
            stack = stack + i
        else :
            answer += i
        
        if stack in num :
            answer += str(num.index(stack))
            stack = ""
    return int(answer)

s = "one4seveneight"
print(solution(s))