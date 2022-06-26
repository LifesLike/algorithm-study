def solution(records):
    nicknames = {}
    answer = []

    for record in records:
        line = record.split(' ')
        if len(line) == 3:
            status, uid, nickname = line
            nicknames[uid] = nickname

    for record in records:
        line = record.split(' ')
        status, uid = line[0], line[1]

        if status == 'Enter':
            answer.append("{}님이 들어왔습니다." .format(nicknames[uid]))
        elif status == 'Leave':
            answer.append("{}님이 나갔습니다." .format(nicknames[uid]))

    return answer


if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
