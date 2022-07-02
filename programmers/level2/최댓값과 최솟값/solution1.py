def solution(s):
    nums = sorted(list(map(int, s.split())))
    return " ".join(map(str, (nums[0], nums[-1])))


if __name__ == '__main__':
    s = "-1 -2 -3 -4"
    print(solution(s))
