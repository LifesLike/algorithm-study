

import sys


# 연결 리스트 기반 풀이 => 시간 초과
def move_cursor(log: list, cur: int, direction: str):
    if direction == '<':
        next_pos = max(0, cur - 1)
    else:
        next_pos = min(len(log), cur + 1)

    return next_pos


def delete(log: list, cur: int):
    if cur < 1:
        return cur
    log.pop(cur - 1)
    return cur - 1


if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    arrow = ['<', '>']
    backspace = '-'

    for _ in range(test_case):
        key_log = sys.stdin.readline().strip()
        pswd = []
        idx = 0

        for ch in key_log:
            if ch in arrow:
                idx = move_cursor(pswd, idx, ch)
                continue
            if ch == backspace:
                idx = delete(pswd, idx)
                continue

            pswd.insert(idx, ch)
            idx += 1

        print("".join(pswd))
