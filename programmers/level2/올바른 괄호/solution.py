def solution(s):
    pair = 0
    for parenthesis in s:
        if pair < 0:
            return False
        if parenthesis == '(':
            pair += 1
        else:
            pair -= 1

    return pair == 0


if __name__ == '__main__':
    s = "()()"
    print(solution(s))
