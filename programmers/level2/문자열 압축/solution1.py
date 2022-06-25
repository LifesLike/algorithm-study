def solution(s):
    answer = s
    for stride in range(1, len(s) // 2 + 2):
        temp = ""
        compressed = 1
        prev = s[0: stride]
        for i in range(stride, len(s), stride):
            sub_string = s[i: i + stride]
            if prev == sub_string:
                compressed += 1
            else:
                if compressed > 1:
                    temp += str(compressed) + prev
                else:
                    temp += prev
                compressed = 1
                prev = sub_string

        if compressed > 1:
            temp += str(compressed) + prev
        else:
            temp += prev

        answer = min(answer, temp, key=len)

    return len(answer)


if __name__ == '__main__':
    s = "a"
    print(solution(s))
