def solution(s):
    answer = []
    for sequence in s.split(' '):
        if len(sequence) == 1:
            answer.append(sequence[0].upper())
        elif len(sequence) > 1:
            answer.append(sequence[0].upper() + sequence[1:].lower())
        else:
            answer.append('')

    return " ".join(answer)


if __name__ == '__main__':
    # s = "3people unFollowed me"
    s = "3 S   n"
    print(solution(s))
