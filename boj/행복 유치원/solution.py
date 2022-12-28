import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    members = list(map(int, sys.stdin.readline().split()))
    diff = []
    for i in range(n - 1):
        diff.append(members[i + 1] - members[i])

    diff.sort()
    print(sum(diff[:n - k]))
