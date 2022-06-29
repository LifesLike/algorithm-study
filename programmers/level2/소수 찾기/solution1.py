import itertools as it


def solution(numbers):
    primes = [True for _ in range(10000000)]
    primes[0] = primes[1] = False
    answer = 0
    limit = int(10000000 ** 0.5) + 1

    for i in range(2, limit):
        if primes[i]:
            for j in range(i + i, limit, i):
                primes[j] = False

    for i in range(1, len(numbers) + 1):
        permutations = it.permutations(numbers, i)

        for permutation in permutations:
            idx = int("".join(permutation))
            if primes[idx]:
                primes[idx] = False
                answer += 1

    return answer


if __name__ == '__main__':
    numbers = "17"
    print(solution(numbers))
