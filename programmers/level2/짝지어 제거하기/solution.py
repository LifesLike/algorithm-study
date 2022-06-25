def solution(s):
    sequence = [s[0]]

    for c in s[1:]:
        if sequence and sequence[-1] == c:
            sequence.pop()
        else:
            sequence.append(c)

    return 0 if sequence else 1


if __name__ == '__main__':
    s = "baabaa"
    print(solution(s))
