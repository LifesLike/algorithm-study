def solution(citations):
    citations.sort()

    for i, citation in enumerate(citations):
        if len(citations) - i <= citation:
            return len(citations) - i

    return 0


if __name__ == '__main__':
    # citations = [3, 9, 6, 1, 5]
    # citations = [1, 4, 4, 4]
    # citations = [1, 1, 1, 1, 2, 2]
    citations = [0]
    print(solution(citations))
