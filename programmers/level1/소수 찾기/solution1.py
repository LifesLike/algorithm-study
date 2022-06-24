def solution(n):
    count = 0

    for i in range(2, n + 1):
        if isprime(i):
            count += 1

    return count


def isprime(number):
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = 10
    print(solution(n))
