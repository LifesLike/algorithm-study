def solution(id_list, report, k):
    reports = {}
    banned = {}

    for uid in id_list:
        reports[uid] = []
        banned[uid] = 0

    for one in report:
        src, tgt = one.split()
        if tgt not in reports[src]:
            reports[src].append(tgt)
            banned[tgt] += 1

    alarm = [0 for _ in range(len(id_list))]

    for i, uid in enumerate(id_list):
        for reported in reports[uid]:
            if banned[reported] >= k:
                alarm[i] += 1

    return alarm


if __name__ == '__main__':
    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))