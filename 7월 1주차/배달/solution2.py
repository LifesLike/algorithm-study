from math import inf
import heapq


def solution(N, road, K):
    town = {i: {} for i in range(N)}

    for src, dst, weight in road:
        src -= 1
        dst -= 1
        town[src][dst] = min(town[src].get(dst, inf), weight)
        town[dst][src] = town[src][dst]

    distance = [inf for _ in range(N)]
    distance[0] = 0
    queue = [(0, 0)]
    heapq.heapify(queue)

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for dst, weight in town[node].items():
            new_cost = weight + dist
            if new_cost < distance[dst]:
                distance[dst] = new_cost
                heapq.heappush(queue, (new_cost, dst))

    return sum(map(lambda x: x <= K, distance))


if __name__ == '__main__':
    N = 6
    road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    K = 4
    print(solution(N, road, K))
