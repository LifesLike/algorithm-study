def solution(numbers, target):
    return dfs(numbers, 0, 0, target)


def dfs(numbers, cur_depth, cur_values, target):
    answer = 0

    if cur_depth == len(numbers):
        if cur_values == target:
            return 1
        return 0

    answer += dfs(numbers, cur_depth + 1, cur_values + numbers[cur_depth], target)
    answer += dfs(numbers, cur_depth + 1, cur_values - numbers[cur_depth], target)

    return answer


if __name__ == '__main__':
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))
