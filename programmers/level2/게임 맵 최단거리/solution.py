from collections import deque


def solution(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = True

    queue = deque()
    queue.append((0, 0, 1))

    n, m = len(maps) - 1, len(maps[0]) - 1

    while queue:
        i, j, depth = queue.popleft()

        if i == n and j == m:
            return depth

        if i - 1 >= 0 and maps[i - 1][j] and not visited[i - 1][j]:
            queue.append((i - 1, j, depth + 1))
            visited[i - 1][j] = True
        if j + 1 <= m and maps[i][j + 1] and not visited[i][j + 1]:
            queue.append((i, j + 1, depth + 1))
            visited[i][j + 1] = True
        if i + 1 <= n and maps[i + 1][j] and not visited[i + 1][j]:
            queue.append((i + 1, j, depth + 1))
            visited[i + 1][j] = True
        if j - 1 >= 0 and maps[i][j - 1] and not visited[i][j - 1]:
            queue.append((i, j - 1, depth + 1))
            visited[i][j - 1] = True

    return -1


if __name__ == '__main__':
    maps = [[0]]
    print(solution(maps))
