from math import ceil, floor


# === 시간 초과 === #
def solution(w, h):
    w, h = min(w, h), max(w, h)
    prev_h = 0
    count = 0

    for i in range(1, w + 1):
        cur_h = h * i / w
        count += ceil(cur_h) - prev_h
        prev_h = floor(cur_h)

    return w * h - count


if __name__ == '__main__':
    w, h = 100000000, 100000000
    print(solution(w, h))