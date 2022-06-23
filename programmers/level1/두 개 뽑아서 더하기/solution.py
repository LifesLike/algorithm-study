import itertools as it


def solution(numbers):
    answer = [0 for _ in range(201)]
    combinations = it.combinations(numbers, 2)

    for combination in combinations:
        answer[sum(combination)] = 1

    return [i for i in range(201) if answer[i]]


if __name__ == '__main__':
    numbers = [2, 1, 3, 4, 1]
    print(solution(numbers))
