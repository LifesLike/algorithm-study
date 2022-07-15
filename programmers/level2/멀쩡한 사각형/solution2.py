from math import gcd


def solution(w, h):
    return w * h - w - h + gcd(w, h)


if __name__ == '__main__':
    print(solution(3, 5))