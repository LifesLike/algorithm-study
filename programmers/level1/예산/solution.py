def solution(d, budget):
    d.sort()
    count = 0

    for request in d:
        budget -= request
        if budget < 0:
            break
        count += 1

    return count


if __name__ == '__main__':
    d = [1,3,2,5,4]
    budget = 9
    print(solution(d, budget))
