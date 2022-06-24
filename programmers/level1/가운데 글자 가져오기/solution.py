def solution(s):
    mid = len(s) // 2
    if len(s) % 2 != 0:
        return s[mid]

    return s[mid - 1: mid + 1]


if __name__ == '__main__':
    s = "abcde"
    print(solution(s))
