def solution(n, words):
    history = [words[0]]
    wrong_position = 0

    for i, word in enumerate(words[1:]):
        if history[-1][-1] != word[0] or word in history:
            wrong_position = i + 1
            break
        history.append(word)

    return [wrong_position % n + 1, wrong_position // n + 1] if wrong_position else [0, 0]


if __name__ == '__main__':
    n = 5
    words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
             "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    print(solution(n, words))
