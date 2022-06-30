def solution(n):
    answer = [[0 for _ in range(i + 1)] for i in range(n)]
    value = 1

    i, j = -1, 0

    for direction in range(n):
        for _ in range(direction, n):
            if direction % 3 == 0:
                i += 1
            elif direction % 3 == 1:
                j += 1
            else:
                i -= 1
                j -= 1
            answer[i][j] = value
            value += 1

    return [i for line in answer for i in line]


if __name__ == '__main__':
    n = 4
    print(solution(n))
