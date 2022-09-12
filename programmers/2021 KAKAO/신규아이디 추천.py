from curses.ascii import isalpha


def solution(new_id):
    #1
    new_id = new_id.lower()
    
    new_id = list(new_id)
    answer = []
    check = 0

    #2
    for i in range(len(new_id)) :
        if  1 == new_id[i].isalnum() or new_id[i] == "-" or new_id[i] == "_" :
            check = 0
            answer.append(new_id[i])
        elif new_id[i] == "." : #3
            if check == 0 : 
                check = 1
                answer.append(new_id[i])

    #4
    if len(answer) != 0 and answer[0] == "." : answer.pop(0)
    if len(answer) != 0 and answer[len(answer) - 1] == "." : answer.pop(len(answer) - 1)

    #5
    if len(answer) == 0 : answer.append("a")

    #6
    if len(answer) >= 16 :
        answer = answer[0:15]
        if answer[14] == "." : answer.pop(14)

    #7
    while len(answer) <= 2 : 
        answer = answer + list(answer[len(answer) - 1])
    
    answer = "".join(answer)
    return answer

print(solution("abcdefghijklmn.p"))