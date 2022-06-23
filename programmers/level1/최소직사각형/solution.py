def solution(sizes):
    for i, size in enumerate(sizes):
        w, h = size
        if w < h:
            sizes[i] = h, w

    sorted_sizes = list(zip(*sizes))
    w_max = max(sorted_sizes[0])
    h_max = max(sorted_sizes[1])

    return w_max * h_max


if __name__ == '__main__':
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))
