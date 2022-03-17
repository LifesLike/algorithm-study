import math
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))

    payment = [math.inf for _ in range(N + 1)]
    payment[0] = 0

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            payment[i] = min(payment[i], payment[i-j] + cards[j-1])

    print(payment[-1])
