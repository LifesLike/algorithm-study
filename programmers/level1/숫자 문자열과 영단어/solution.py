def solution(sequence):
    number = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
              "eight": 8, "nine": 9, "ten": 10}

    answer = ""
    substr = ""

    for s in sequence:
        if s.isdigit():
            answer += s
            continue
        substr += s
        if substr in number:
            answer += str(number[substr])
            substr = ""

    return int(answer)


if __name__ == '__main__':
    s = "one4seveneight"
    print(solution(s))
