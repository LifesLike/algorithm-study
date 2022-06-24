def solution(arr1, arr2):
    answer = []
    for row1, row2 in zip(arr1, arr2):
        answer.append([sum(element) for element in zip(row1, row2)])

    return answer


if __name__ == '__main__':
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]
    print(solution(arr1, arr2))
