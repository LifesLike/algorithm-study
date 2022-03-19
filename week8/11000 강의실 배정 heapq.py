import heapq
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    lectures = []
    rooms = []

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        lectures.append((start, end))

    lectures.sort()

    for start, end in lectures:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    print(len(rooms))
