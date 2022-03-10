import sys

if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().split())
    lines = []

    for _ in range(K):
        lines.append(int(sys.stdin.readline()))

    start = 0
    end = max(lines)
    target_length = 1

    while start <= end:
        cnt = 0
        cut_length = (start + end) // 2

        if cut_length > 0:
            for line in lines:
                cnt += line // cut_length

        if cnt >= N:
            target_length = cut_length
            start = cut_length + 1
        else:
            end = cut_length - 1

    print(target_length)
