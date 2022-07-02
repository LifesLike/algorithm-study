def solution(s):
    nums = list(map(int, s.split()))
    return " ".join(map(str, (min(nums), max(nums))))


if __name__ == '__main__':
    s = "-1 -2 -3 -4"
    print(solution(s))
