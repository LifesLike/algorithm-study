def solution(skill, skill_trees):
    skill_length = len(skill)
    answer = 0

    for skill_tree in skill_trees:
        skill_limit = 0
        possible = True

        for cur_skill in skill_tree:
            if cur_skill in skill:
                if cur_skill != skill[skill_limit]:
                    possible = False
                    break
                else:
                    skill_limit += 1
            if skill_limit == skill_length:
                break
        if possible:
            answer += 1

    return answer


if __name__ == '__main__':
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))
