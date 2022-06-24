def solution(n):
    x = int(n ** (1/2))
    if x**2 == n:
        return (x+1) ** 2
    return -1


if __name__ == '__main__':
    n = 121
    print(solution(n))
