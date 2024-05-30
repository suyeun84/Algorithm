import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    bus = []
    d = [int(1e9) for _ in range(N+1)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        bus.append([A,B,C])

    d[1] = 0
    flag = False
    for i in range(N): #최소 거리는 N-1번 돌면 나옴
        for j in bus:
            start, end, dist = j
            # 음수 사이클 판별
            if i == N - 1:
                if d[start] == int(1e9):
                    continue
                if d[end] > d[start] + dist:
                    flag = True
                    break
                else:
                    continue
            if d[start] == int(1e9):
                continue
            if d[end] > d[start] + dist:
                d[end] = d[start] + dist

    if flag:
        print(-1)
    else:
        for i in range(2, N+1):
            if d[i] == int(1e9):
                print(-1)
            else:
                print(d[i])


if __name__ == '__main__':
    solution()
