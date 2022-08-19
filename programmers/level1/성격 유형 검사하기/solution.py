def solution(survey, choices):
    mbti = {i: 0 for i in ["R", "T", "C", "F", "J", "M", "A", "N"]}
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

    for item, choice in zip(survey, choices):
        if choice < 4:
            mbti[item[0]] += scores[choice]
        else:
            mbti[item[1]] += scores[choice]

    result = ""
    if mbti["R"] < mbti["T"]:
        result += "T"
    else:
        result += "R"
    if mbti["C"] < mbti["F"]:
        result += "F"
    else:
        result += "C"
    if mbti["J"] < mbti["M"]:
        result += "M"
    else:
        result += "J"
    if mbti["A"] < mbti["N"]:
        result += "N"
    else:
        result += "A"

    return result


if __name__ == '__main__':
    survey = ["AN", "CF", "MJ", "RT", "NA"]
    choices = [5, 3, 2, 7, 5]
    print(solution(survey, choices))
