def solution(numbers):
    answer = []

    for number in numbers:
        next_num = number + 1
        bit_diff = bin(next_num ^ number).count('1')

        if bit_diff <= 2:
            answer.append(next_num)
        else:
            answer.append(next_num + int('1'*(bit_diff - 2), 2))

    return answer


if __name__ == '__main__':
    numbers = [2, 7]
    print(solution(numbers))
