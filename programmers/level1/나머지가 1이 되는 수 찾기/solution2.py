def solution(n):
    if n % 2 != 0:
        return 2

    n -= 1

    for i in range(3, int(n ** (1 / 2)) + 1, 2):
        if n % i == 0:
            return i

    return n


if __name__ == '__main__':
    n = 12
    print(solution(n))
