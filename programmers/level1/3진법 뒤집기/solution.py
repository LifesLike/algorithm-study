def solution(n):
    remainder = n
    ternary = ""
    while remainder > 0:
        ternary += str(remainder % 3)
        remainder //= 3

    decimal = 0

    for i, digit in enumerate(ternary[::-1]):
        decimal += int(digit) * (3 ** i)

    return decimal


if __name__ == '__main__':
    n = 45
    print(solution(n))
