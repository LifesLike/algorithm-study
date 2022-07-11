def solution(m, n, board):
    board = [list(column) for column in zip(*board)]

    while True:
        remove_positions = []
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j].isalpha() and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    remove_positions.append((i, j))

        if not remove_positions:
            break

        for i, j in remove_positions:
            board[i][j] = board[i+1][j] = board[i][j+1] = board[i+1][j+1] = " "

        compressed = []
        for line in board:
            compressed.append(list("".join(line)
                                   .replace(" ", "")
                                   .rjust(m, " ")))

        board = compressed

    return sum(line.count(' ') for line in board)


if __name__ == '__main__':
    m, n = 6, 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    print(solution(m, n, board))
