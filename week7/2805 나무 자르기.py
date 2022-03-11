import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))

    start = 1
    end = max(trees)
    solution = 0

    while start <= end:
        cut_length = (start + end) // 2
        remainder = 0

        for tree in trees:
            remainder += max(0, tree - cut_length)

        if remainder >= M:
            solution = cut_length
            start = cut_length + 1
        else:
            end = cut_length - 1

    print(solution)
