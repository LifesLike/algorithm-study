
# 16시 03분 시작
# 16시 26분 종료

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    test_cases = []

    for _ in range(T):
        height, width, N = map(int, sys.stdin.readline().split())

        horizontal = (N - 1) // height + 1
        vertical = (N - 1) % height + 1
        room = vertical * 100 + horizontal
        print(room)
