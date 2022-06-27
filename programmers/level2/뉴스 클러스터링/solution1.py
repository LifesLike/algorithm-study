from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = []
    set2 = []

    for i in range(len(str1) - 1):
        sub_str = str1[i: i + 2]
        if sub_str.isalpha():
            set1.append(sub_str)

    for i in range(len(str2) - 1):
        sub_str = str2[i: i + 2]
        if sub_str.isalpha():
            set2.append(sub_str)

    if not set1 and not set2:
        return 65536

    set1_count = Counter(set1)
    set2_count = Counter(set2)

    union = 0
    intersection = 0

    for key, value in set1_count.items():
        if key in set2_count:
            intersection += min(value, set2_count[key])
            union += max(value, set2_count[key])
        else:
            union += value

    for key, value in set2_count.items():
        if key in set1_count:
            continue
        union += value

    return int(intersection / union * 65536)


if __name__ == '__main__':
    str1 = "FRANCE"
    str2 = "french"
    print(solution(str1, str2))
