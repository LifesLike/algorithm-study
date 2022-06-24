def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


if __name__ == '__main__':
    strings = ["abce", "abcd", "cdx"]
    n = 2
    print(solution(strings, n))
