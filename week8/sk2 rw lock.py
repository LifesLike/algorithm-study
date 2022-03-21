from queue import PriorityQueue


def solution(arr: list, processes: list):
    working = PriorityQueue()
    waiting = PriorityQueue()
    result = []
    reading = False

    elem = 0
    used_time = 0

    # i 는 시간
    for i in range(1, 2000):
        if not working.empty():
            used_time += 1

        while not working.empty():
            if working.queue[0] <= i:
                working.get()
            else:
                break

        if working.empty():
            reading = False

        if elem < len(processes) and i == int(processes[elem].split()[1]):
            splitted = processes[elem].split()
            splitted[1] = int(splitted[1])
            if working.empty():
                if splitted[0] == "read":
                    working.put(max(int(splitted[1]) + int(splitted[2]), i + int(splitted[2])))
                    reading = True
                    result.append("".join(arr[int(splitted[3]): int(splitted[4]) + 1]))
                else:
                    working.put(max(int(splitted[1]) + int(splitted[2]), i + int(splitted[2])))
                    reading = False
                    for i in range(int(splitted[3]), int(splitted[4]) + 1):
                        arr[i] = splitted[-1]
            elif reading and splitted[0] == "read" and waiting.empty():
                working.put(max(int(splitted[1]) + int(splitted[2]), i + int(splitted[2])))
                result.append("".join(arr[int(splitted[3]): int(splitted[4]) + 1]))
            else:
                if splitted[0] == "read":
                    waiting.put((2, splitted))
                else:
                    waiting.put((1, splitted))
            elem += 1

        if working.empty() and not waiting.empty():
            if waiting.queue[0][0] == 1:
                _, splitted, = waiting.get()
                working.put(max(int(splitted[1]) + int(splitted[2]), i + int(splitted[2])))
                reading = False
                for i in range(int(splitted[3]), int(splitted[4]) + 1):
                    arr[i] = splitted[-1]
            else:
                while not waiting.empty():
                    if waiting.queue[0][0] == 2:
                        _, splitted, = waiting.get()
                        working.put(max(int(splitted[1]) + int(splitted[2]), i + int(splitted[2])))
                        reading = True
                        result.append("".join(arr[int(splitted[3]): int(splitted[4]) + 1]))

        if reading and not waiting.empty() and waiting.queue[0][0] == 2:
            while not waiting.empty():
                if waiting.queue[0][0] == 2:
                    _, splitted, = waiting.get()
                    working.put(max(int(splitted[1]) + int(splitted[2]), i + int(splitted[2])))
                    reading = True
                    result.append("".join(arr[int(splitted[3]): int(splitted[4]) + 1]))
                else:
                    break

        if elem >= len(processes) and working.empty() and waiting.empty():
            break

    result.append(str(used_time))
    return result


if __name__ == '__main__':
    # arr = ["1", "2", "4", "3", "3", "4", "1", "5"]
    # processes = ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]
    arr = ["1","1","1","1","1","1","1"]
    processes = ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
    print(solution(arr, processes))
