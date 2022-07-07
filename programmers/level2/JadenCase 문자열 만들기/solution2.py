# str.capitalize() vs str.title() 차이 주의하기!!
def solution(s):
    answer = []
    for sequence in s.split(' '):
        answer.append(sequence.capitalize())

    return " ".join(answer)


if __name__ == '__main__':
    s = "3people unFollowed me"
    # s = "3 S   n"
    print(solution(s))
