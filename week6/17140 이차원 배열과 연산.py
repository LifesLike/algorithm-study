import collections
import sys


def operation_r(matrix: list):
    for row in matrix:
        counter = collections.Counter(row)
        del counter[0]
        row.clear()
        for t in sorted(counter.items(), key=lambda x: (x[1], x[0])):
            row.append(t[0])
            row.append(t[1])

    max_row_length = min(len(max(matrix, key=len)), 100)

    for row in matrix:
        row.extend([0 for _ in range(max_row_length - len(row))])


if __name__ == '__main__':
    r, c, k = map(int, sys.stdin.readline().split())
    r -= 1
    c -= 1
    took_time = -1
    arr = []

    for _ in range(3):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(101):
        if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
            took_time = i
            break

    #     R연산
        if len(arr) >= len(arr[0]):
            operation_r(arr)
    #     C연산
        else:
            arr = list(map(list, zip(*arr)))
            operation_r(arr)
            arr = list(map(list, zip(*arr)))

    print(took_time)

