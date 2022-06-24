# 에라토스테네스의 체
def solution(n):
    primes = [True for _ in range(n+1)]

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i + i, n + 1, i):
                primes[j] = False

    print(primes)
    return primes.count(True) - 2


if __name__ == '__main__':
    n = 10
    print(solution(n))
