
import sys

if __name__ == '__main__':
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        logger = sys.stdin.readline().strip()
        pswd = []
        secondary = []

        for ch in logger:
            if ch == '-':
                if pswd:
                    pswd.pop()
                continue
            if ch == '<':
                if pswd:
                    secondary.append(pswd.pop())
                continue
            if ch == '>':
                if secondary:
                    pswd.append(secondary.pop())
                continue
            else:
                pswd.append(ch)

        print("".join(pswd + secondary[::-1]))
