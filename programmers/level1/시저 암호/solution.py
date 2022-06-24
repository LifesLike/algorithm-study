def solution(s, n):
    answer = ""
    lower_start = ord('a')
    upper_start = ord('A')

    for ch in s:
        if ch == ' ':
            answer += ch
        else:
            if 'a' <= ch <= 'z':
                moved = lower_start + (ord(ch) - lower_start + n) % 26
            else:
                moved = upper_start + (ord(ch) - upper_start + n) % 26
            answer += chr(moved)

    return answer


if __name__ == '__main__':
    s = "a B z"
    n = 4
    print(solution(s, n))
