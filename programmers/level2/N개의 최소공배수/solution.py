from collections import deque
from math import gcd


def solution(arr):
    if len(arr) == 1:
        return arr[0]

    arr = deque(arr)
    while len(arr) > 1:
        num1, num2 = arr.popleft(), arr.popleft()
        arr.append(num1*num2 // gcd(num1, num2))

    return arr[0]


if __name__ == '__main__':
    arr = [2, 6, 8, 14]
    print(solution(arr))
