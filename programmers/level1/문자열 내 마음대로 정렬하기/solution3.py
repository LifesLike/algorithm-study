def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


if __name__ == '__main__':
    strings = ["abce", "abcd", "cdx"]
    n = 2
    print(solution(strings, n))
