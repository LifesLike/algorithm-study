import math


def solution(money, costs):
    production = [math.inf for _ in range(money + 1)]
    coins = [1, 5, 10, 50, 100, 500]

    production[0] = 0

    for j in range(1, money + 1):
        for i in range(6):
            if coins[i] <= j:
                production[j] = min(production[j], production[j - coins[i]] + costs[i])

    return production[-1]


if __name__ == '__main__':
    print(solution(4578, [1, 4, 99, 35, 50, 1000]))
