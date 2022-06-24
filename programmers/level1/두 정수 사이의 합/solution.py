def solution(a, b):
    a, b = min(a, b), max(a, b)

    return (b * (b + 1) // 2) - (a * (a - 1) // 2)


if __name__ == '__main__':
    a = 3
    b = 5
    print(solution(a, b))
