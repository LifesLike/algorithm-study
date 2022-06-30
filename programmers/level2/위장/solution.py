def solution(clothes):
    cabinet = {key: 0 for _, key in clothes}

    for val, key in clothes:
        cabinet[key] += 1

    answer = 1
    for val in cabinet.values():
        answer *= (val + 1)

    return answer - 1


if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
