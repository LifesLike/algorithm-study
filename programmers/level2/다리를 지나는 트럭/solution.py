from collections import deque


def solution(bridge_length, limit, truck_weights):
    weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)], maxlen=bridge_length)
    cur_weight = 0
    runtime = 0

    while cur_weight or weights:
        runtime += 1
        cur_weight -= bridge.popleft()

        if weights and cur_weight + weights[0] <= limit:
            truck = weights.popleft()
            bridge.append(truck)
            cur_weight += truck
        else:
            bridge.append(0)

    return runtime


if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))
