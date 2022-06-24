def solution(dartResult):
    dartResult = dartResult.replace("10", "t")
    reformat = dartResult[0]

    for c in dartResult[1:]:
        if c.isdigit() or c == 't':
            reformat += ' '
        reformat += c

    total_score = 0
    prev_score = 0

    for result in reformat.split():
        option = ""
        if len(result) == 3:
            score, bonus, option = result
        else:
            score, bonus = result

        if score == 't':
            score = 10
        score = int(score)

        if bonus == 'D':
            score **= 2
        elif bonus == 'T':
            score **= 3

        if option:
            if option == '*':
                score *= 2
                prev_score *= 2
            elif option == '#':
                score = -score

        total_score += prev_score
        prev_score = score

    return total_score + prev_score


if __name__ == '__main__':
    dartResult = "1D2S#10S"
    print(solution(dartResult))
