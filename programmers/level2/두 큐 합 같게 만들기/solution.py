from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    push_pop_cnt = 0
    limit = len(queue1)

    if (queue1_sum + queue2_sum) % 2 != 0:
        return -1

    while push_pop_cnt < 2 * limit:
        if queue1_sum == queue2_sum:
            return push_pop_cnt
        if queue1_sum > queue2_sum:
            popped = queue1.popleft()
            queue2.append(popped)
            queue2_sum += popped
            queue1_sum -= popped
        else:
            popped = queue2.popleft()
            queue1.append(popped)
            queue1_sum += popped
            queue2_sum -= popped
        push_pop_cnt += 1

    return -1


if __name__ == '__main__':
    # queue1 = [3, 2, 7, 2]
    # queue2 = [4, 6, 5, 1]
    # queue1 = [1, 2, 1, 2]
    # queue2 = [1, 10, 1, 2]

    queue1 = [3, 2, 7, 3]
    queue2 = [4, 6, 5, 6]
    print(solution(queue1, queue2))
