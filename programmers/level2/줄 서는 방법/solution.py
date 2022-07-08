from itertools import permutations


def solution(n, k):
    for i, permutation in enumerate(permutations(range(1, n+1), n)):
        if i == k-1:
            return permutation


if __name__ == '__main__':
    n = 3
    k = 5
    print(solution(n, k))
