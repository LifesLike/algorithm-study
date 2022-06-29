from collections import deque


def solution(priorities, location):
    pair = [(p, i) for i, p in enumerate(priorities)]
    queue = deque(pair)
    order = 0

    while True:
        if queue[0] == max(queue, key=lambda x: x[0]):
            job, idx = queue.popleft()
            order += 1
            if idx == location:
                return order
        else:
            queue.rotate(-1)


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))
