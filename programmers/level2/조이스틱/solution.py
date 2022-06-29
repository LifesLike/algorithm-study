def solution(target):
    a_ascii = ord('A')
    z_ascii = ord('Z')
    positions = [i for i in range(len(target)) if target[i] != 'A']
    answer = positions[-1] if positions else 0

    # index 0부터 시작하는 경우, 뒤로 먼저 가는 경우 모두 고려
    for i in range(len(positions) - 1):
        answer = min(answer, 2 * positions[i] + len(target) - positions[i + 1],
                     2 * (len(target) - positions[i + 1]) + positions[i])

    for i, name in enumerate(target):
        answer += min(ord(name) - a_ascii, z_ascii - ord(name) + 1)
    return answer


if __name__ == '__main__':
    target = "BBBBAAAAAAAB"
    print(solution(target))
