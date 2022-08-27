def solution(board):
    row = len(board)
    col = len(board[0])
    max_size = 0

    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1 and board[i-1][j] != 0 and board[i-1][j-1] != 0 and board[i][j-1] != 0:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                max_size = max(max_size, board[i][j])

    if max_size == 0:
        max_size = max(max_size, max(map(max, board)))

    return max_size ** 2


if __name__ == '__main__':
    board = [[0], [1], [1], [1]]
    print(solution(board))
