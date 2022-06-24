def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')


if __name__ == '__main__':
    s = "pPooooyY"
    print(solution(s))
