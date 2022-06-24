def solution(string_sequence):
    answer = []
    for string in string_sequence.split(' '):
        even = True
        line = ""
        for s in string:
            if even:
                line += s.upper()
            else:
                line += s.lower()
            even = not even
        answer.append(line)

    return " ".join(answer)


if __name__ == '__main__':
    s = "fff     ss d"
    print(solution(s))
