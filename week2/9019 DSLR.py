
# 14시 34분 시작
import queue
import sys


class Node:
    def __init__(self, value, command, parent):
        self.__value = value
        self.__command = command
        self.__parent = parent

    def get_value(self):
        return self.__value

    def get_command(self):
        return self.__command

    def get_parent(self):
        return self.__parent


def double(value):
    return 2 * value % 10000


def store(value):
    if value == 0:
        return 9999
    return value - 1


def left(value):
    temp = four_digit(value)
    result = "".join(map(str, temp[1:])) + temp[0]
    return int(result)


def right(value):
    temp = four_digit(value)
    result = temp[-1] + "".join(map(str, temp[:3]))
    return int(result)


def four_digit(value):
    temp = list(map(str, str(value)))
    temp = ['0'] * (4 - len(temp)) + temp
    return temp


# def a_star_search(start_val, target_val):
#     open_list = queue.PriorityQueue()
#     open_list.put((0, Node(start_val, None, None)))
#     close_list = []
#
#     depth = 0
#
#     while not open_list.empty():
#         node = open_list.get()
#
#         if node[1].get_value() == target_val:
#             # do something
#             route = back_track(node[1])
#             break
#
#         depth += 1
#
#         D = double(node[1].get_value())
#         S = store(node[1].get_value())
#         L = left(node[1].get_value())
#         R = right(node[1].get_value())
#
#         open_list.put((abs(target_val - D) + depth, Node(D, 'D', node[1])))
#         open_list.put((abs(target_val - S) + depth, Node(S, 'S', node[1])))
#         open_list.put((abs(target_val - L) + depth, Node(L, 'L', node[1])))
#         open_list.put((abs(target_val - R) + depth, Node(R, 'R', node[1])))
#
#     return route


def bfs(start_val, target_val):
    bfs_queue = queue.Queue()
    bfs_queue.put(Node(start_val, None, None))

    while not bfs_queue.empty():
        node = bfs_queue.get()
        if node.get_value() == target_val:
            return back_track(node)


        D = double(node.get_value())
        S = store(node.get_value())
        L = left(node.get_value())
        R = right(node.get_value())

        bfs_queue.put(Node(D, 'D', node))
        bfs_queue.put(Node(S, 'S', node))
        bfs_queue.put(Node(L, 'L', node))
        bfs_queue.put(Node(R, 'R', node))

    return


def back_track(node: Node):
    route = [node.get_command()]
    parent: Node = node.get_parent()
    while True:
        if parent.get_command():
            route.append(parent.get_command())
        else:
            break
        parent: Node = parent.get_parent()

    return route


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        start, target = map(int, sys.stdin.readline().split())
        result = bfs(start, target)
        print("".join(map(str, result)))
