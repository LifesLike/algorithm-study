def solution(nums):
    return min(len(set(nums)), len(nums)//2)


if __name__ == '__main__':
    nums = [3, 1, 2, 3]
    print(solution(nums))