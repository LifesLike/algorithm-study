def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)

    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                reserve.remove(i - 1)
                answer += 1
            elif i + 1 in reserve:
                reserve.remove(i + 1)
                answer += 1
        else:
            answer += 1

    return answer


if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    print(solution(n, lost, reserve))
