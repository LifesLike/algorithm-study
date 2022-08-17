def solution(msg):
    word_map = {chr(word): i + 1 for i, word in enumerate(range(ord('A'), ord('Z') + 1))}
    next_index = 27

    accum = ""
    indices = []
    last_index = 0

    for word in msg:
        accum += word
        if accum not in word_map:
            word_map[accum] = next_index
            next_index += 1
            accum = word
            indices.append(last_index)
        last_index = word_map[accum]

    indices.append(last_index)

    return indices


if __name__ == '__main__':
    msg = "TOBEORNOTTOBEORTOBEORNOT"
    print(solution(msg))
