
# 14시 58분 시작
# 15시 25분 종료


import sys


def calc(postfix_operation: str, operand: dict):
    stack = []
    operators = ['+', '-', '*', '/']

    for i in postfix_operation:
        if i in operators:
            var2 = stack.pop()
            var1 = stack.pop()
            result = 0

            if i == '+':
                result = var1 + var2
            elif i == '-':
                result = var1 - var2
            elif i == '*':
                result = var1 * var2
            elif i == '/':
                result = var1 / var2

            stack.append(result)
        else:
            stack.append(operand[i])

    return stack[0]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    postfix = sys.stdin.readline().strip()
    operand = {}
    unicode_start = ord('A')

    for i in range(N):
        operand[chr(unicode_start + i)] = int(sys.stdin.readline())

    result = calc(postfix, operand)

    print("%0.2f" % result)

