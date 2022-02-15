import sys


# 최소 공배수 풀이 => 시간 초과
# n % M == n % N 인 n을 찾기
def calender(M, N, x, y):
    if M % 2 == 0 and N % 2 == 0:
        limit = M * N // 2
    else:
        limit = M * N
    for i in range(x, limit + 1, M):
        for j in range(y, i + 1, N):
            if i == j:
                return j

    return -1


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())
    for _ in range(test_case):
        M, N, x, y, = map(int, sys.stdin.readline().split())
        print(calender(M, N, x, y))
