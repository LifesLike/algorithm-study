import sys

if __name__ == '__main__':
    N, M = map(int, input().split())

    if N == 1 or M == 1:
        print(1)
    elif N < 3:
        print(min(4, (M + 1) // 2))
    elif M <= 6:
        print(min(4, M))
    else:
        print(M - 2)
