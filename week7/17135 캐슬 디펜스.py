import sys
from itertools import combinations

if __name__ == '__main__':
    N, M, D = map(int, sys.stdin.readline().split())
    field = []

    for _ in range(N):
        field.append(list(map(int, sys.stdin.readline().split())))

    combination = combinations(range(M), 3)
    max_point = 0

    for ar1, ar2, ar3, in combination:
        cur_point = 0
        position = []

        for cnt in range(N - 1, -1, -1):
            ar1_shot = ar2_shot = ar3_shot = False

            for d in range(1, D + 1):
                for i in range(cnt, -1, -1):
                    for j in range(M):
                        if field[i][j] and (i, j) not in position:
                            if not ar1_shot and cnt + 1 - i + abs(ar1 - j) <= d:
                                ar1_shot = True
                                if (i, j) not in position:
                                    cur_point += 1
                                    position.append((i, j))
                            elif not ar2_shot and cnt + 1 - i + abs(ar2 - j) <= d:
                                ar2_shot = True
                                if (i, j) not in position:
                                    cur_point += 1
                                    position.append((i, j))
                            elif not ar3_shot and cnt + 1 - i + abs(ar3 - j) <= d:
                                ar3_shot = True
                                if (i, j) not in position:
                                    cur_point += 1
                                    position.append((i, j))

        max_point = max(max_point, cur_point)

    print(max_point)
