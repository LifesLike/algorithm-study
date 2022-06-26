def solution(parenthesis):
    if not parenthesis:
        return ""

    stack = []
    for p in parenthesis:
        stack.append(p)
        if stack.count('(') == stack.count(')'):
            break

    u = "".join(stack)
    v = parenthesis[len(stack):]

    if isright(u):
        return u + solution(v)

    new_str = '(' + solution(v) + ')'

    u = u[1: -1]
    u = "".join(map(lambda s: '(' if s == ')' else ')', u))

    return new_str + u


def isright(w):
    stack = []

    for p in w:
        if p == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(p)

    return not stack


if __name__ == '__main__':
    p = "()))((()"
    print(solution(p))
