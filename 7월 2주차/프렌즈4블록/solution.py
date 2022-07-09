def solution(m, n, board):
    board = [list(board[i]) for i in range(len(board))]

    while True:
        remove_positions = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j].isalpha() and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    remove_positions.append((i, j))

        for i, j in remove_positions:
            board[i][j] = board[i+1][j] = board[i][j+1] = board[i+1][j+1] = " "

        board = list(map(list, zip(*board)))
        columns = []
        for line in board:
            columns.append(list("".join(line).replace(" ", "").rjust(m, " ")))

        board = list(map(list, zip(*columns)))

        if not remove_positions:
            break

    return sum(line.count(' ') for line in board)


if __name__ == '__main__':
    m, n = 6, 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    print(solution(m, n, board))
