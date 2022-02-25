import math
import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    stats = list(map(int, sys.stdin.readline().split()))
    stats.sort()

    left = 0
    right = N - 1
    best = math.inf
    best_left = best_right = 0

    while left < right:
        value = stats[left] + stats[right]
        abs_value = abs(value)

        if abs_value < best:
            best = abs_value
            best_left = left
            best_right = right

        if value > 0:
            right -= 1
        else:
            left += 1

    print(stats[best_left], stats[best_right])
