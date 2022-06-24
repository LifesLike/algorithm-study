def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if not answer:
        answer = [-1]
    return answer


if __name__ == '__main__':
    arr = [5, 9, 7, 10]
    divisor = 5
    print(solution(arr, divisor))
