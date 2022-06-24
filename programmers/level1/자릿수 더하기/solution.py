def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)

    return answer


if __name__ == '__main__':
    N = 123
    print(solution(N))
