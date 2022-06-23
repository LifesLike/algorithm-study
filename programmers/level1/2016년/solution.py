def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = 0

    for i in range(a - 1):
        day_of_year += day_of_month[i]

    day_of_year += b

    return day[(day_of_year - 1) % 7]


if __name__ == '__main__':
    a = 5
    b = 24
    print(solution(a, b))
