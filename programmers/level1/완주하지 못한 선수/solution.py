def solution(participant, completion):
    participants = {x: 0 for x in participant}

    for key in participant:
        participants[key] += 1

    for key in completion:
        participants[key] -= 1

    for key, value in participants.items():
        if value:
            return key


if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))