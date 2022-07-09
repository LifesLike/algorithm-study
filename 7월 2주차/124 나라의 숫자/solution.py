def solution(n):
    answer = ""
    while n >= 3:
        n, remainder = divmod(n, 3)
        if remainder == 0:
            remainder = 4
            n -= 1
        answer += str(remainder)

    if n != 0:
        answer += str(n)

    return answer[::-1]


if __name__ == '__main__':
    for i in range(1, 10):
        print(solution(i))
