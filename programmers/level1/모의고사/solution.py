def solution(answers):
    result = []
    sol1 = [1, 2, 3, 4, 5]
    sol2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sol3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct1 = correct2 = correct3 = 0

    for i, answer in enumerate(answers):
        if sol1[i % len(sol1)] == answer:
            correct1 += 1
        if sol2[i % len(sol2)] == answer:
            correct2 += 1
        if sol3[i % len(sol3)] == answer:
            correct3 += 1

    max_correct = max(correct1, correct2, correct3)
    if max_correct == correct1:
        result.append(1)
    if max_correct == correct2:
        result.append(2)
    if max_correct == correct3:
        result.append(3)

    return result


if __name__ == '__main__':
    answers = [1, 2, 3, 4, 5]
    print(solution(answers))