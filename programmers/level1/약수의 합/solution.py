def solution(n):
    if n < 2:
        return n

    answer = n + 1

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            answer += i
            if i ** 2 != n:
                answer += n // i

    return answer


if __name__ == '__main__':
    n = 16
    print(solution(n))
