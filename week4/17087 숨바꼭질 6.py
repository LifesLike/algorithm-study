import math
import sys


if __name__ == '__main__':
    N, cur_pos = map(int, sys.stdin.readline().split())
    brothers = list(map(int, sys.stdin.readline().split()))

    diffs = [abs(brothers[i] - cur_pos) for i in range(len(brothers))]

    closest = min(diffs)

    for diff in diffs:
        closest = math.gcd(closest, diff)

    print(closest)
