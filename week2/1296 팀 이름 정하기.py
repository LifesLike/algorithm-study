
# 14시 42분 시작
# 14시 57분 종료

import sys


def formula(name: str, team_name: str):
    l = name.count("L") + team_name.count("L")
    o = name.count("O") + team_name.count("O")
    v = name.count("V") + team_name.count("V")
    e = name.count("E") + team_name.count("E")

    return ((l + o)*(l + v)*(l + e)*(o + v)*(o + e)*(v + e)) % 100


if __name__ == '__main__':
    eng_name = sys.stdin.readline().strip()
    N = int(sys.stdin.readline())
    best_probability = -1
    best_name = ""

    for _ in range(N):
        candidate = sys.stdin.readline().strip()
        probability = formula(eng_name, candidate)
        if probability > best_probability:
            best_probability = probability
            best_name = candidate
        elif probability == best_probability:
            best_name = candidate if candidate < best_name else best_name

    print(best_name)
