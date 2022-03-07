import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    cases = []

    for _ in range(T):
        cases.append(int(sys.stdin.readline()))

    one_two_three = [[0, 0, 0] for _ in range(max(cases))]

    one_two_three[0][0] = 1
    one_two_three[1][1] = 1
    one_two_three[2][0] = one_two_three[2][1] = one_two_three[2][2] = 1

    for i in range(3, len(one_two_three)):
        one_two_three[i][0] = one_two_three[i-1][1] + one_two_three[i-1][2]
        one_two_three[i][1] = one_two_three[i-2][0] + one_two_three[i-2][2]
        one_two_three[i][2] = one_two_three[i-3][0] + one_two_three[i-3][1]

    for case in cases:
        print(sum(one_two_three[case-1]) % 1000000009)
