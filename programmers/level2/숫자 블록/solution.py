# 효율성테스트에서 시간초과가 아닌 실패
def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        divisors = []
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0 and i // j <= 10000000:
                divisors.append(j)
                if j**2 != i and i // j <= 10000000:
                    divisors.append(i // j)
        if len(divisors) < 2:
            answer.append(1)
        else:
            answer.append(sorted(divisors)[-2])

    if begin == 1:
        answer[0] = 0

    return answer


if __name__ == '__main__':
    begin, end = 10000000, 10000010
    print(solution(begin, end))
