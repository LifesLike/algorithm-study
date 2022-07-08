def solution(n):
    jump = [0 for _ in range(2001)]
    jump[1] = 1
    jump[2] = 2

    for i in range(3, n+1):
        jump[i] = (jump[i-1] + jump[i-2]) % 1234567

    return jump[n]


if __name__ == '__main__':
    n = 4
    print(solution(n))
