def solution(arr):
    size = len(arr)

    # 이 부분 추가하면 답 틀림. 왜?
    # if size == 1:
    #     if arr[0] == 0:
    #         return 1, 0
    #     return 0, 1

    one_in_arr = 0
    for line in arr:
        one_in_arr += sum(map(lambda x: x == 1, line))

    if one_in_arr == size**2:
        return 0, 1
    if one_in_arr == 0:
        return 1, 0
    else:
        return list(map(sum, zip(
            solution([row[: size//2] for row in arr[: size//2]]), solution([row[size//2:] for row in arr[: size//2]]),
            solution([row[: size//2] for row in arr[size//2:]]), solution([row[size//2:] for row in arr[size//2:]]))
            ))


if __name__ == '__main__':
    arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    print(solution(arr))
