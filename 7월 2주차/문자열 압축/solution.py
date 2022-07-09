from math import inf, ceil


def solution(s):
    answer = inf
    for stride in range(1, ceil(len(s) / 2) + 1):
        temp = ""
        repeat = 1
        compressed = s[0: stride]
        for i in range(stride, len(s), stride):
            substr = s[i: i+stride]
            if compressed == substr:
                repeat += 1
            else:
                if repeat > 1:
                    temp += str(repeat)
                temp += compressed
                compressed = substr
                repeat = 1
        if repeat > 1:
            temp += str(repeat)
        temp += compressed
        answer = min(answer, len(temp))

    return answer


if __name__ == '__main__':
    s = "aabbaccc"
    print(solution(s))
