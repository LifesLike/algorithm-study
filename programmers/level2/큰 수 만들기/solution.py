def solution(number, k):
    stack = []

    for n in number:
        if k > 0:
            while stack and stack[-1] < n and k > 0:
                stack.pop()
                k -= 1
        stack.append(n)

    return "".join(stack[:len(stack) - k])


if __name__ == '__main__':
    number = "81"
    k = 1
    print(solution(number, k))
