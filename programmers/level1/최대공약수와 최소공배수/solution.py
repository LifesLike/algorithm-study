# 파이썬 3.9 미만은 math 모듈 lcm 함수 못 씀
from math import gcd


def solution(n, m):
    return [gcd(n, m), n*m // gcd(n, m)]


if __name__ == '__main__':
    n, m = 3, 12
    print(solution(n, m))
