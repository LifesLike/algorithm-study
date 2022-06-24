def solution(n):
    return list(map(int, reversed(str(n))))


if __name__ == '__main__':
    n = 12345
    print(solution(n))
