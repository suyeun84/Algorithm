import sys
import math


def solution():
    input = sys.stdin.readline
    wheel = [list(map(int, input().strip())) for _ in range(4)]
    K = int(input())
    answer = 0

    def turn_clock(num):
        tmp = [0] * 8
        for i in range(8):
            tmp[i] = wheel[num][i]
        wheel[num][0] = tmp[7]
        for i in range(1, 8):
            wheel[num][i] = tmp[i-1]

    def turn_rev_clock(num):
        tmp = [0]*8
        for i in range(8):
            tmp[i] = wheel[num][i]
        wheel[num][7] = tmp[0]
        for i in range(0, 7):
            wheel[num][i] = tmp[i+1]

    for _ in range(K):
        num, dir = map(int, input().split())
        n = num-1
        d = [0]*4
        d[n] = dir
        for i in range(n+1, 4):
            if wheel[i-1][2] != wheel[i][6]:
                if d[i-1] == -1:
                    d[i] = 1
                else:
                    d[i] = -1
            else:
                break

        for i in range(n-1, -1, -1):
            if wheel[i+1][6] != wheel[i][2]:
                if d[i+1] == -1:
                    d[i] = 1
                else:
                    d[i] = -1
            else:
                break
        for i in range(4):
            if d[i] == 0:
                continue
            elif d[i] == 1:
                turn_clock(i)
            elif d[i] == -1:
                turn_rev_clock(i)

    for i in range(4):
        if wheel[i][0] == 1:
            answer += math.pow(2, i)
    print(int(answer))


if __name__ == '__main__':
    solution()
