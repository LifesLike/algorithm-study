import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    woods = [int(sys.stdin.readline()) for _ in range(N)]

    highest = 0
    cnt = 0
    for w in woods[::-1]:
        if highest < w:
            cnt += 1
        highest = max(highest, w)

    print(cnt)
