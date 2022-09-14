def solution(survey, choices):
    check = [0,7,6,5,4,3,2,1]
    type = {"RT" : [0, 0], "CF" : [0, 0], "JM" : [0, 0], "AN" : [0, 0]}
    for x in survey :
        score = choices.pop(0)
        if x == "TR" or x == "FC" or x == "MJ" or x == "NA" :
            x = list(x)
            x[0], x[1] = x[1], x[0]
            score = check[score]
            x = ''.join(x)

        if score < 4 :
            type[x][0] += 4 - score
        elif score == 4 : 
            pass
        else :
            type[x][1] += score - 4

    print(type)
    answer = ""
    ke = ["RT", "CF", "JM", "AN"]
    for i in ke : 
        if type[i][0] >= type[i][1] : answer = answer + i[0]
        else : answer = answer + i[1]
        
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
solution(survey, choices)