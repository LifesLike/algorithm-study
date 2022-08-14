import itertools as it


# === 테스트 케이스 2개 시간 초과 === #
def solution(orders, courses):
    answer = []
    alphabet = []

    for order in orders:
        for ch in order:
            if ch not in alphabet:
                alphabet.append(ch)

    alphabet.sort()

    for course in courses:
        combinations = it.combinations(alphabet, course)
        temp = []

        for combination in combinations:
            contain = 0
            for order in orders:
                found = True
                for comb in combination:
                    if comb not in order:
                        found = False
                        break
                if found:
                    contain += 1

            if contain > 1:
                temp.append((contain, "".join(combination)))

        if temp:
            dd = list(filter(lambda x: x[0] == max(temp)[0], temp))
            answer.extend(list(zip(*dd))[1])

    return sorted(answer)

if __name__ == '__main__':
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    courses = [2, 3, 5]
    print(solution(orders, courses))
