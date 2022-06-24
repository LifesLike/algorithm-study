def solution(arr):
    answer = [arr[0]]
    answer.extend([arr[i] for i in range(1, len(arr)) if arr[i] != arr[i-1]])
    return answer


if __name__ == '__main__':
    arr = [1, 1, 3, 3, 0, 1, 1]
    print(solution(arr))
