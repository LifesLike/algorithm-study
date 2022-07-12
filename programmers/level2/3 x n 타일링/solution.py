def solution(n):
    answer = [0 for _ in range(5001)]
    answer[2] = 3
    for i in range(4, n + 1, 2):
        case = answer[i-2] * 3 + 2
        for j in range(2, i - 2):
            case += answer[j] * 2
        answer[i] = case % 1000000007

    return answer[n]


if __name__ == '__main__':
    n = 4
    print(solution(n))
