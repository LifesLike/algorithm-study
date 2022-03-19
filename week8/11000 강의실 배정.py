import queue
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    lectures = []
    rooms = queue.PriorityQueue()

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        lectures.append((start, end))

    lectures.sort(key=lambda x: x[0])

    for start, end in lectures:
        if rooms.qsize() > 0 and rooms.queue[0] <= start:
            rooms.get()
        rooms.put(end)

    print(rooms.qsize())

# 7
# 7 8
# 3 7
# 1 5
# 5 9
# 0 2
# 6 8
# 1 6