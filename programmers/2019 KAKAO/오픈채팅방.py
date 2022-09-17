def solution(record):
    for i in range(len(record)) :
        record[i] = record[i].split(" ");
    print(record)
    id = {}
    for i in record :
        if i[0] != "Leave" : id[i[1]] = i[2]
    answer = []
    for i in record :
        if i[0] == "Enter" :
            answer.append("{}님이 들어왔습니다.".format(id[i[1]]))
        elif i[0] == "Leave" :
            answer.append("{}님이 나갔습니다.".format(id[i[1]]))
    print(answer)
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

solution(record)