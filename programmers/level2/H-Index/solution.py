def solution(citations):
    citations.sort()
    length = len(citations)

    for i, h in enumerate(citations):
        if length - i <= h:
            return length - i
    return 0


if __name__ == '__main__':
    citation = [0]
    print(solution(citation))
