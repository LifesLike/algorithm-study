from math import inf


def solution(N, road, K):
    graph = [[inf for _ in range(N)] for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0

    for v1, v2, weight in road:
        v1 -= 1
        v2 -= 1
        graph[v1][v2] = min(graph[v1][v2], graph[v2][v1], weight)
        graph[v2][v1] = min(graph[v2][v1], graph[v1][v2])

    for c in range(N):
        for i in range(N):
            if i == c:
                continue
            for j in range(N):
                if j == c or j == i:
                    continue
                graph[i][j] = min(graph[i][j], graph[i][c] + graph[c][j])

    return sum(map(lambda x: x <= K, graph[0]))


if __name__ == '__main__':
    N = 5
    road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3
    print(solution(N, road, K))
