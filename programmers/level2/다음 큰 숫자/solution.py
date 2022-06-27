def solution(n):
    answer = n + 1
    one = bin(n)[2:].count('1')
    while True:
        if bin(answer)[2:].count('1') == one:
            return answer
        answer += 1


if __name__ == '__main__':
    n = 78
    print(solution(n))
    