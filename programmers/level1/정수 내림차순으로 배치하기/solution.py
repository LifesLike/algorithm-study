def solution(n):
    return int("".join(sorted(str(n), reverse=True)))


if __name__ == '__main__':
    n = 118372
    print(solution(n))
