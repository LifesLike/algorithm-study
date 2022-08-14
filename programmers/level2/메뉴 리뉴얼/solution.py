from itertools import combinations


def solution(orders, courses):
    orders = [sorted(order) for order in orders]
    logs = []
    answers = []

    for course_count in courses:
        limit = 0
        temp = []
        for menus in orders:
            for combination in combinations(menus, course_count):
                common = 0
                if combination not in logs:
                    logs.append(combination)
                    for others in orders:
                        if all(menu in others for menu in combination):
                            common += 1
                    if common > 1 and common > limit:
                        limit = common
                        temp = [combination]
                    elif common > 1 and common == limit:
                        temp.append(combination)
        answers.extend(temp)

    return sorted(["".join(menu) for menu in answers])


if __name__ == '__main__':
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]

    print(solution(orders, course))
