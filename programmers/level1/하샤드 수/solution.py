def solution(x):
    x_sum = sum(map(int, str(x)))
    return x % x_sum == 0


if __name__ == '__main__':
    x = 13
    print(solution(x))
