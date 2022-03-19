import heapq
import sys


class MyPQ:
    def __init__(self):
        self.queue = []

    def put(self, item):
        heapq.heappush(self.queue, item)

    def get(self):
        return heapq.heappop(self.queue)

    def qsize(self):
        return len(self.queue)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    lectures = []
    rooms = MyPQ()

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        lectures.append((start, end))

    lectures.sort(key=lambda x: x[0])

    for start, end in lectures:
        if rooms.qsize() > 0 and rooms.queue[0] <= start:
            rooms.get()
        rooms.put(end)

    print(rooms.qsize())
