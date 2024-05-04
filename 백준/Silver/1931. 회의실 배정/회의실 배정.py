import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    M = []
    for _ in range(N):
        S, E = map(int, input().split())
        M.append([E, S])

    M.sort()
    curr = 0
    cnt = 0
    for T in M:
        if T[1] >= curr:
            cnt +=1
            curr = T[0]

    print(cnt)


if __name__ == '__main__':
    solution()