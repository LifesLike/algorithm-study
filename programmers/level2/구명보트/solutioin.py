def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boat = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boat += 1

    return boat


if __name__ == '__main__':
    people = [10, 90, 10, 90, 100, 10, 10, 10]
    limit = 100
    print(solution(people, limit))
    