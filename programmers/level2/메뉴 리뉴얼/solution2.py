from itertools import combinations
from collections import Counter


# Counter 이용한 풀이
def solution(orders, courses):
    orders = [sorted(order) for order in orders]
    answers = []

    for course_count in courses:
        combs = []
        for order in orders:
            combs.extend(combinations(order, course_count))

        common = Counter(combs).most_common()
        answers.extend([key for key, val in common if val == common[0][1] and val > 1])

    return sorted(["".join(answer) for answer in answers])


if __name__ == '__main__':
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]

    print(solution(orders, course))
