def solution(numbers, target):
    answer = 0
    max_depth = len(numbers)

    def dfs(cur_idx, cur_numbers):
        if cur_idx == max_depth:
            if cur_numbers == target:
                nonlocal answer
                answer += 1
            return

        dfs(cur_idx + 1, cur_numbers + numbers[cur_idx])
        dfs(cur_idx + 1, cur_numbers - numbers[cur_idx])

    dfs(0, 0)

    return answer


if __name__ == '__main__':
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))
