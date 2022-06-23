import math


def solution(left, right):
    partial_sum = 0

    for i in range(left, right + 1):
        sqrt = int(math.sqrt(i))
        if sqrt ** 2 == i:
            partial_sum -= i
        else:
            partial_sum += i

    return partial_sum


if __name__ == '__main__':
    left = 13
    right = 17
    print(solution(left, right))
