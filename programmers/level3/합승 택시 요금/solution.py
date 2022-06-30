from math import inf


def solution(n, s, a, b, fares):
    graph = [[inf for _ in range(n)] for _ in range(n)]
    s -= 1
    a -= 1
    b -= 1

    for i in range(n):
        graph[i][i] = 0

    for i, j, weight in fares:
        i -= 1
        j -= 1
        graph[i][j] = weight
        graph[j][i] = weight

    for c in range(n):
        for i in range(n):
            if i == c:
                continue
            for j in range(n):
                if j == i or j == c:
                    continue
                graph[i][j] = min(graph[i][j], graph[i][c] + graph[c][j])

    min_cost = inf

    for waypoint in range(n):
        min_cost = min(min_cost, graph[s][waypoint] + graph[waypoint][a] + graph[waypoint][b])

    return min_cost


if __name__ == '__main__':
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))
