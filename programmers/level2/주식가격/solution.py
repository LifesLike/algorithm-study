def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []
    for i, price in enumerate(prices):
        if stack and stack[-1][0] > price:
            while stack and stack[-1][0] > price:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
        stack.append((price, i))

    return answer


if __name__ == '__main__':
    prices = [3, 2, 1, 2, 3]
    print(solution(prices))
