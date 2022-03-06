import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    memo = {}

    for _ in range(N):
        address, password = map(str, sys.stdin.readline().split())
        memo[address] = password

    for _ in range(M):
        address = sys.stdin.readline().strip()
        print(memo[address])
