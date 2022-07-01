def solution(s):
    x_removed = 0
    iteration = 0
    while s != '1':
        iteration += 1
        prev_length = len(s)
        s = s.replace("0", "")
        x_removed += prev_length - len(s)
        s = bin(len(s))[2:]

    return iteration, x_removed


if __name__ == '__main__':
    s = "110010101001"
    print(solution(s))
