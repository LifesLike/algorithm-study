def solution(n):
    digit = ""
    while (n):
        n, mod = divmod(n, 3)
        if mod == 0:
            mod = 4
            n -= 1
        digit += str(mod)

    return digit[::-1]


if __name__ == '__main__':
    n = 18
    print(solution(n))
