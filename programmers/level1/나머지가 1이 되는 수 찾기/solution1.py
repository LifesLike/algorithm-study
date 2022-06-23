def solution(n):
    if n % 2 != 0:
        return 2

    for i in range(3, n, 2):
        if n % i == 1:
            return i


if __name__ == '__main__':
    n = 10
    print(solution(n))
