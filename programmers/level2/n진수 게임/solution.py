def solution(n, t, m, p):
    tube = ""
    length = 0
    p -= 1
    cur = 0
    prev = -1

    while length < t:
        next_num = get_next(n, prev + 1)
        prev += 1
        for num in next_num:
            if length == t:
                break
            if cur == p:
                tube += num
                length += 1
            cur = (cur + 1) % m

    return tube


def get_next(n, next):
    digit = ""
    if next == 0:
        return "0"
    while next:
        next, remainder = divmod(next, n)
        if remainder >= 10:
            remainder = chr(ord('A') + remainder - 10)
        digit = str(remainder) + digit

    return digit


if __name__ == '__main__':
    n, t, m, p = 16, 16, 2, 2
    print(solution(n, t, m, p))
