import math


def solution(n, s, a, b, fares):
    costs = [[math.inf for _ in range(n)] for _ in range(n)]

    # 자기 자신과의 거리는 0
    for i in range(n):
        costs[i][i] = 0

    for fare in fares:
        costs[fare[0]-1][fare[1]-1] = fare[2]
        costs[fare[1]-1][fare[0]-1] = fare[2]

    for c in range(n):
        for i in range(n):
            if i == c:
                continue
            for j in range(n):
                if i == j or j == c:
                    continue
                costs[i][j] = min(costs[i][j], costs[i][c] + costs[c][j])

    mini = math.inf
    for c in range(n):
        mini = min(mini, costs[s-1][c] + costs[c][a-1] + costs[c][b-1])


    return mini


if __name__ == '__main__':
    fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    print(solution(7, 3, 4, 1, fares))