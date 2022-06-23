from collections import Counter


def solution(N, stages):
    users = len(stages)
    counter = Counter(stages)
    counter = dict(sorted(counter.items()))
    fail_rate = [[0, i + 1] for i in range(N)]

    for key, val in counter.items():
        if key == N + 1:
            continue
        fail_rate[key - 1][0] = val / users
        users -= val

    fail_rate.sort(key=lambda x: (-x[0], x[1]))

    return list(zip(*fail_rate))[1]


if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
