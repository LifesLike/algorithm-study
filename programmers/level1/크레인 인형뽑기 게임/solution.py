def solution(board, moves):
    stack = []
    point = 0

    for j in moves:
        j -= 1
        for line in board:
            if line[j]:
                if stack and stack[-1] == line[j]:
                    stack.pop()
                    point += 2
                else:
                    stack.append(line[j])
                line[j] = 0
                break

    return point


if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))
