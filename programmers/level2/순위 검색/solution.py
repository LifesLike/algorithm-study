def solution(infos, queries):
    db = {
        "java": {"frontend": {"junior": {"pizza": [],
                                         "chicken": []},
                              "senior": {"pizza": [],
                                         "chicken": []}},
                 "backend": {"junior": {"pizza": [],
                                        "chicken": []},
                             "senior": {"pizza": [],
                                        "chicken": []}}
                 },
        "python": {"frontend": {"junior": {"pizza": [],
                                           "chicken": []},
                                "senior": {"pizza": [],
                                           "chicken": []}},
                   "backend": {"junior": {"pizza": [],
                                          "chicken": []},
                               "senior": {"pizza": [],
                                          "chicken": []}}
                   },
        "cpp": {"frontend": {"junior": {"pizza": [],
                                        "chicken": []},
                             "senior": {"pizza": [],
                                        "chicken": []}},
                "backend": {"junior": {"pizza": [],
                                       "chicken": []},
                            "senior": {"pizza": [],
                                       "chicken": []}}
                }
    }

    result = []

    for info in infos:
        language, apply, career, food, score = info.split()
        db[language][apply][career][food].append(int(score))

    for query in queries:
        query = query.replace("and", "")
        language, apply, career, food, score = query.split()

        if language == '-':
            languages = ["java", "python", "cpp"]
        else:
            languages = [language]
        if apply == '-':
            applies = ["frontend", "backend"]
        else:
            applies = [apply]
        if career == '-':
            careers = ["junior", "senior"]
        else:
            careers = [career]
        if food == '-':
            foods = ["pizza", "chicken"]
        else:
            foods = [food]

        select = []
        for lan in languages:
            for app in applies:
                for car in careers:
                    for snack in foods:
                        select.extend(db[lan][app][car][snack])

        result.append(sum(map(lambda x: x >= int(score), select)))

    return result


if __name__ == '__main__':
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150",
            "cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100",
             "- and - and - and - 150"]
    print(solution(info, query))
