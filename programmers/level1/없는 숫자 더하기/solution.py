def solution(numbers):
    onetoten = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    result = onetoten - set(numbers)
    return sum(result)


if __name__ == '__main__':
    nums = [1,2,3,4,6,7,8,0]
    print(solution(nums))
