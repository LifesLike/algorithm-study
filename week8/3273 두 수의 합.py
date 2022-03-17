import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    x = int(sys.stdin.readline())

    start = 0
    end = n - 1
    cnt = 0

    while start < end:
        part = nums[start] + nums[end]
        if part == x:
            cnt += 1
            end -= 1
        elif part > x:
            end -= 1
        else:
            start += 1

    print(cnt)
