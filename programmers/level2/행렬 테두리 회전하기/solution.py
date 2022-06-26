from collections import deque


def solution(rows, columns, queries):
    matrix = [[j * columns + i for i in range(1, columns + 1)] for j in range(rows)]
    answer = []

    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        queue = deque()

        for j in range(y1, y2 + 1):
            queue.append(matrix[x1][j])
        for i in range(x1 + 1, x2 + 1):
            queue.append(matrix[i][y2])
        for j in range(y2 - 1, y1 - 1, -1):
            queue.append(matrix[x2][j])
        for i in range(x2 - 1, x1, -1):
            queue.append(matrix[i][y1])

        queue.rotate(1)
        answer.append(min(queue))
        idx = 0
        for j in range(y1, y2 + 1):
            matrix[x1][j] = queue[idx]
            idx += 1
        for i in range(x1 + 1, x2 + 1):
            matrix[i][y2] = queue[idx]
            idx += 1
        for j in range(y2 - 1, y1 - 1, -1):
            matrix[x2][j] = queue[idx]
            idx += 1
        for i in range(x2 - 1, x1, -1):
            matrix[i][y1] = queue[idx]
            idx += 1

    return answer


if __name__ == '__main__':
    rows = 100
    columns = 97
    queries = [[1, 1, 100, 97]]
    print(solution(rows, columns, queries))
