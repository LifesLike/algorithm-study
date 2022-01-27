import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    DNAs = []
    super_gene = []
    distance = 0

    for _ in range(N):
        DNAs.append(sys.stdin.readline().strip())

    for j in range(M):
        dna_cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for i in range(N):
            dna_key = DNAs[i][j]
            dna_cnt[dna_key] += 1

        primary_dna = sorted(dna_cnt.items(), key=lambda d: d[1], reverse=True)
        super_gene.append(primary_dna[0][0])
        distance += N - primary_dna[0][1]

    print(''.join(super_gene))
    print(distance)
