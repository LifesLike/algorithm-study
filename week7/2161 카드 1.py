import collections

if __name__ == '__main__':
    n = int(input())
    dequeue = collections.deque([i for i in range(1, n + 1)])
    result = []

    while dequeue:
        if len(dequeue) == 1:
            result.append(dequeue[0])
            break

        result.append(dequeue.popleft())
        dequeue.append(dequeue.popleft())

    print(" ".join(map(str, result)))
