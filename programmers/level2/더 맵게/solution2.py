import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    iteration = 0
    food1 = heapq.heappop(scoville)
    while food1 < K:
        if len(scoville) < 1:
            return -1

        food2 = heapq.heappop(scoville)
        food1 = heapq.heappushpop(scoville, food1 + food2 * 2)
        iteration += 1

    return iteration


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))
