import sys


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    number = sys.stdin.readline().strip()

    stack = []

    for n in number:
        if K > 0:
            while K > 0 and stack and stack[-1] < n:
                stack.pop()
                K -= 1
        stack.append(n)

    print("".join(stack[:len(stack)-K]))
