import math
from itertools import combinations


def solution(nums):
    answer = 0
    combination = combinations(nums, 3)

    for comb in combination:
        if isprime(sum(comb)):
            answer += 1

    return answer


def isprime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    nums = [1, 2, 7, 6, 4]
    print(solution(nums))