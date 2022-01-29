
# 16시 28분 시작
# 16시 34분 종료

import sys

if __name__ == '__main__':
    target = int(sys.stdin.readline())
    binary = []
    
    while target > 0:
        binary.append(target % 2)
        target //= 2

    print(''.join(map(str, binary[::-1])))
