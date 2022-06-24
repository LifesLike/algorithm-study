def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        final = bin(a | b)[2:].zfill(n)
        line = ""
        for i in final:
            if i == "1":
                line += "#"
            else:
                line += " "
        answer.append(line)

    return answer


if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
