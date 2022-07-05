from itertools import combinations


def solution(relation):
    relation = list(zip(*relation))
    candidates = []

    for i in range(1, len(relation) + 1):
        for combination in combinations(range(len(relation)), i):
            flag = True

            for candidate in candidates:
                if all(elem in combination for elem in candidate):
                    flag = False
                    break

            if flag:
                temp = []
                for idx in combination:
                    temp.append(relation[idx])

                if len(set(zip(*temp))) == len(relation[0]):
                    candidates.append(combination)

    return len(candidates)


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
                ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))
