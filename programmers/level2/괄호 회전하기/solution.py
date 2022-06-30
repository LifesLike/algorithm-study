from collections import deque


def solution(s):
    queue = deque(s)
    answer = 0
    for _ in range(len(s)):
        if iscorrect("".join(queue)):
            answer += 1
        queue.rotate(-1)

    return answer


def iscorrect(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack:
                return False
            elif stack[-1] == pairs[ch]:
                stack.pop()
        else:
            stack.append(ch)

    return not stack

if __name__ == '__main__':
    s = "[](){}"
    print(solution(s))
