def solution(numbers, hand):
    answer = ""
    left_fixed = [1, 4, 7]
    right_fixed = [3, 6, 9]
    if hand == "right":
        default = "R"
    else:
        default = "L"

    column = {2: 0, 5: 1, 8: 2, 0: 3}
    shortest = [[3, 2, 1, 0], [1, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 4], [2, 1, 2, 3], [1, 0, 1, 2], [2, 1, 2, 3],
                [3, 2, 1, 2], [2, 1, 0, 1], [3, 2, 1, 2]]

    special = [4, 3, 2, 1]

    left_prev_position = '*'
    right_prev_position = '#'

    for number in numbers:
        if number in left_fixed:
            answer += "L"
            left_prev_position = number
            continue
        elif number in right_fixed:
            answer += "R"
            right_prev_position = number
            continue
        else:
            col = column[number]
            if left_prev_position == '*':
                left_shortest = special[col]
            else:
                left_shortest = shortest[left_prev_position][col]
            if right_prev_position == '#':
                right_shortest = special[col]
            else:
                right_shortest = shortest[right_prev_position][col]

            if right_shortest == left_shortest:
                answer += default
                if default == 'R':
                    right_prev_position = number
                else:
                    left_prev_position = number
            elif right_shortest < left_shortest:
                answer += 'R'
                right_prev_position = number
            else:
                answer += 'L'
                left_prev_position = number

    return answer


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    print(solution(nums, hand))
