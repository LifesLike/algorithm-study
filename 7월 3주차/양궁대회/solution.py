from itertools import combinations


def solution(n, info):
    biggest = 1     # 라이언과 어피치의 최대 점수 차이. 동점인 경우 라이언의 패배이기 때문에 초기값은 1로 세팅
    answers = []    # 라이언의 가능한 점수 후보 리스트

    for i in range(1, 12):
        for candidates in combinations(range(11), i):     # candidates: 0점 ~ 10점 사이에서 라이언이 맞춘 과녁 점수 후보들의 조합
            remaining = n                       # 남은 화살 수
            balance = 0                         # 라이언과 어피치의 점수 차이
            scores = [0 for _ in range(11)]     # 라이언이 쏜 결과
            for score_idx, apeach in enumerate(info):
                if apeach < remaining and score_idx in candidates:    # 이 과녁이 라이언이 맞춘 과녁 후보에 속하는 경우
                    scores[score_idx] = apeach + 1
                    remaining -= apeach + 1     # 어피치보다 한 발은 더 쏴야 라이언이 점수 가져감
                    balance += 10 - score_idx   # 라이언 득점
                elif apeach:
                    balance -= 10 - score_idx   # 어피치 득점
            if remaining:       # 쏠 수 있는 화살이 남은 경우 가장 낮은 점수를 많이 쏘는게 좋음
                scores[-1] += remaining

            if balance == biggest:
                if not any(elem == scores for elem in answers):     # 새로 구한 scores 리스트와 똑같은 값을 가지는 후보가 이미 존재하면 무시
                    answers.append(scores)
            elif balance > biggest:
                biggest = balance
                answers.clear()
                answers.append(scores)

    if not answers:
        return [-1]

    elem_sum = [sum(10**(i + 1)*val for i, val in enumerate(elem)) for elem in answers]     # 가장 낮은 점수를 더 많이 맞춘 후보를 찾기 위해 가장 낮은 자리부터 10^n 의 가중치를 부여
    return answers[elem_sum.index(max(elem_sum))]   # 위에서 구한 가중치들 중 최대값의 후보 리턴


if __name__ == '__main__':
    n = 10
    info = [0,0,0,0,0,0,0,0,3,4,3]
    print(solution(n, info))
