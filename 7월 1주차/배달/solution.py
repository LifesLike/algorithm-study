from math import inf


def solution(N, road, K):
    town = [[inf for _ in range(N)] for _ in range(N)]

    for i in range(N):
        town[i][i] = 0

    for src, dst, weight in road:
        src -= 1
        dst -= 1
        town[src][dst] = min(town[src][dst], weight)
        town[dst][src] = town[src][dst]

    for c in range(N):
        for i in range(N):
            if i == c:
                continue
            for j in range(N):
                if j == i or j == c:
                    continue
                town[i][j] = min(town[i][j], town[i][c] + town[c][j])

    return sum(map(lambda x: x <= K, town[0]))


if __name__ == '__main__':
    N = 5
    road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3
    print(solution(N, road, K))
