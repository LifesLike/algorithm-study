import sys


def calender(M, N, x, y):
    if M % 2 == 0 and N % 2 == 0:
        limit = M * N // 2
    else:
        limit = M * N

    y %= N

    for i in range(x, limit + 1, M):
        if i % N == y:
            return i

    return -1


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())
    for _ in range(test_case):
        M, N, x, y, = map(int, sys.stdin.readline().split())
        print(calender(M, N, x, y))
