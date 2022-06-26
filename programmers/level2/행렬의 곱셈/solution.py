def solution(arr1, arr2):
    arr2 = list(zip(*arr2))
    answer = []
    for row1 in arr1:
        answer_row = []
        for row2 in arr2:
            answer_row.append(sum(i*j for i, j in zip(row1, row2)))

        answer.append(answer_row)

    return answer


if __name__ == '__main__':
    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    print(solution(arr1, arr2))
