def solution(N, stages):
    player = len(stages)
    answer = [0 for i in range(max(stages))]
    for i in range(1, max(stages)) :
        j = 1
        counter = 0
        while j < len(stages) :
            if i == stages[j] :
                counter += 1 
                stages.pop(j)
                j -= 1
            else : j += 1

        print(counter)
        print(len(stages))
        answer[i- 1] = counter / len(stages)
        print(answer)

    return answer

stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
solution(N, stages)