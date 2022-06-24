def solution(price, money, count):
    return max((price * count * (count+1) // 2) - money, 0)


if __name__ == '__main__':
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))
