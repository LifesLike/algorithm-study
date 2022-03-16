from math import factorial


def solution(width, height, diagonals):
    answer = 0

    for i, j in diagonals:
        part1 = factorial(i - 1 + j) // (factorial(i - 1) * factorial(j))
        part2 = factorial(width - i + height - j + 1) // (factorial(width - i) * factorial(height - j + 1))
        answer += part1 * part2

        part1 = factorial(i + j - 1) // (factorial(i) * factorial(j - 1))
        part2 = factorial(width - i + 1 + height - j) // (factorial(width - i + 1) * factorial(height - j))
        answer += part1 * part2

        answer %= 10000019

    return answer % 10000019


if __name__ == '__main__':
    width = 51
    height = 37
    diagonals = [[17,19]]
    # width = 2
    # height = 2
    # diagonals = [[1,1],[2,2]]
    print(solution(width, height, diagonals))
