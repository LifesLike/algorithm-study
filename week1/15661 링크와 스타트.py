import math
import sys
import itertools


def calc_balance(abilities:[], team: set):
    balance = 0
    permutations = itertools.permutations(team, 2)
    for permutation in permutations:
        balance += abilities[permutation[0]][permutation[1]]

    return balance


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    whole = {_ for _ in range(N)}
    abilities = []
    min_diff = math.inf

    for _ in range(N):
        abilities.append(list(map(int, sys.stdin.readline().split())))

    for i in range(2, N//2 + 1):
        combinations = itertools.combinations(whole, i)
        for combination in combinations:
            if N % 2 == 0 and i == N//2 and combination[0] != 0:
                break
            balance1 = calc_balance(abilities, set(combination))
            balance2 = calc_balance(abilities, whole - set(combination))
            diff = abs(balance1 - balance2)
            if diff < min_diff:
                min_diff = diff

    print(min_diff)
