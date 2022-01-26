import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    DNAs = []

    for _ in range(N):
        DNAs.append(sys.stdin.readline().strip())
    
    candidate_sequence = [{"A": 0, "C": 0, "T": 0, "G": 0} for _ in range(M)]
    distance = 0

    for i in range(N):
        for j in range(M):
            dna_key = DNAs[i][j]
            candidate_sequence[j][dna_key] += 1

    for candidate in candidate_sequence:
        dna = sorted(candidate.items(), key=lambda x: x[1], reverse=True)
        distance += N - dna[0][1]
        print(dna[0][0], end='')

    print("\n{}" .format(distance))
