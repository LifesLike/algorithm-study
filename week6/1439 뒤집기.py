import sys

if __name__ == '__main__':
    nums = sys.stdin.readline().strip()
    different = False
    stack = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] and not different:
            stack += 1
            different = True
        elif nums[i] != nums[i-1]:
            different = False

    print(stack)
