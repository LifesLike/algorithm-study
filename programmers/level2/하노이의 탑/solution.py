pillars = [1, 2, 3]
answer = []


def solution(n):
    move(1, 3, n)
    return answer


def move(src, dst, n):
    if n == 1:
        answer.append((src, dst))
    else:
        waypoint = 6 - src - dst
        move(src, waypoint, n-1)
        move(src, dst, 1)
        move(waypoint, dst, n-1)


if __name__ == '__main__':
    n = 2
    print(solution(n))
