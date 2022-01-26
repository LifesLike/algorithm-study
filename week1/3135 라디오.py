import sys

if __name__ == '__main__':
    cur_frequency, target_frequency = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    favorites = []

    for _ in range(N):
        favorites.append(int(sys.stdin.readline()))

    shortest_moving = abs(cur_frequency - target_frequency)

    for favorite in favorites:
        bypass_moving = abs(favorite - target_frequency) + 1
        if shortest_moving > bypass_moving:
            shortest_moving = bypass_moving

    print(shortest_moving)
