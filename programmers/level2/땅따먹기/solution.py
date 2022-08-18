def solution(lands):

    for i, land in enumerate(lands):
        if i > 0:
            lands[i][0] = land[0] + max(lands[i-1][1], lands[i-1][2], lands[i-1][3])
            lands[i][1] = land[1] + max(lands[i-1][0], lands[i-1][2], lands[i-1][3])
            lands[i][2] = land[2] + max(lands[i-1][0], lands[i-1][1], lands[i-1][3])
            lands[i][3] = land[3] + max(lands[i-1][0], lands[i-1][1], lands[i-1][2])

    return max(lands[-1])


if __name__ == '__main__':
    lands = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
    print(solution(lands))
