import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    road = list(map(int, sys.stdin.readline().split()))
    oil = list(map(int, sys.stdin.readline().split()))

    buy_price = oil[0]
    total_price = buy_price * road[0]

    for i in range(1, N-1):
        if oil[i] < buy_price:
            buy_price = oil[i]
        total_price += buy_price * road[i]

    print(total_price)
