def solution(n):
    left = right = 0
    answer = 0
    numbers = range(1, n+1)
    partial = 1

    while left <= right < len(numbers):
        if partial == n:
            answer += 1
            partial -= numbers[left]
            left += 1
        elif partial < n:
            right += 1
            partial += numbers[right]
        else:
            partial -= numbers[left]
            left += 1

    return answer


if __name__ == '__main__':
    n = 15
    print(solution(n))
