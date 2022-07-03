import itertools as it

def solution(k, dungeons):
    answer = 0
    permutations = it.permutations(dungeons, len(dungeons))

    for permutation in permutations:
        energy = k
        possible = 0
        for req, con in permutation:
            if energy >= req:
                energy -= con
                possible += 1

        answer = max(answer, possible)

    return answer


if __name__ == '__main__':
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))
