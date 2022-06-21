def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()

    zero_count = 0
    correct_count = 0

    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
            continue
        for win_num in win_nums:
            if lotto == win_num:
                correct_count += 1
                break
            elif lotto < win_num:
                break

    best = min(7 - correct_count - zero_count, 6)
    worst = min(7 - correct_count, 6)

    return best, worst


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))