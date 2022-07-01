from collections import deque


def solution(cacheSize, cities):
    cities = list(map(lambda x: x.lower(), cities))
    cache = deque([], cacheSize)
    runtime = 0

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            runtime += 1
        else:
            cache.append(city)
            runtime += 5

    return runtime


if __name__ == '__main__':
    cacheSize = 5
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco",
              "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    print(solution(cacheSize, cities))
