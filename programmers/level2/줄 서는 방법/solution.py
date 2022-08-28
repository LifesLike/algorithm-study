from math import factorial


def solution(n, k):
    result = []
    candidate = [True for _ in range(n+1)]
    candidate[0] = False
    i = 1
    count = n

    while True:
        fac = factorial(n - 1)
        if k > fac:
            k -= fac
            i = candidate.index(True, i + 1)
        else:
            result.append(i)
            candidate[i] = False
            if len(result) == count:
                break
            i = candidate.index(True)
            n -= 1

    return result


if __name__ == '__main__':
    n = 5
    k = 10
    print(solution(n, k))
