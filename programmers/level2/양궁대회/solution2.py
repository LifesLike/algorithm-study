from itertools import combinations


def solution(n, info):
    biggest = 1
    answers = []

    for i in range(1, 12):
        for candidates in combinations(range(11), i):
            remaining = n
            balance = 0
            scores = [0 for _ in range(11)]
            for score, apeach in enumerate(info):
                if score in candidates:
                    if apeach < remaining:
                        scores[score] = apeach + 1
                        remaining -= apeach + 1
                        balance += 10 - score
                    else:
                        scores[score] = 1
                        remaining -= 1
                        balance -= 10 - score
                elif apeach:
                    balance -= 10 - score

            if remaining:
                scores[-1] += remaining

            if balance == biggest:
                if not any(elem == scores for elem in answers):
                    answers.append(scores)
            elif balance > biggest:
                biggest = balance
                answers.clear()
                answers.append(scores)

    if not answers:
        return [-1]

    elem_sum = [sum(10**(i + 1)*val for i, val in enumerate(elem)) for elem in answers]
    return answers[elem_sum.index(max(elem_sum))]


if __name__ == '__main__':
    n = 5
    info = [2,1,1,1,0,0,0,0,0,0,0]
    print(solution(n, info))
