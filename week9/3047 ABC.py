import sys

if __name__ == '__main__':
    numbers = sorted(list(map(int, sys.stdin.readline().split())))
    sequence = sys.stdin.readline().strip()

    for s in sequence:
        if s == 'A':
            print(numbers[0], end=' ')
        elif s == 'B':
            print(numbers[1], end=' ')
        else:
            print(numbers[2], end=' ')
