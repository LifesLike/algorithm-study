import math


def solution(width, height, diagonals):
    answer = 0

    for i, j in diagonals:
        part1 = math.factorial(i - 1 + j) // (math.factorial(i - 1) * math.factorial(j))
        part2 = math.factorial(width - i + height - j + 1) // (math.factorial(width - i) * math.factorial(height - j + 1))
        answer += part1 * part2

        part1 = math.factorial(i + j - 1) // (math.factorial(i) * math.factorial(j - 1))
        part2 = math.factorial(width - i + 1 + height - j) // (math.factorial(width - i + 1) * math.factorial(height - j))
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
