def solution(x, n):
    return [i*x for i in range(1, n+1)]


if __name__ == '__main__':
    x = 2
    n = 5
    print(solution(x, n))
