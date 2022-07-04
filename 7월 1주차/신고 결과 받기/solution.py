def solution(id_list, reports, k):
    block = {id: 0 for id in id_list}
    report_result = {id: [] for id in id_list}

    for report in set(reports):
        src, dst = report.split()
        report_result[src].append(dst)
        block[dst] += 1

    answer = []
    for id in id_list:
        mail = 0
        for dst in report_result[id]:
            if block[dst] >= k:
                mail += 1
        answer.append(mail)

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))
