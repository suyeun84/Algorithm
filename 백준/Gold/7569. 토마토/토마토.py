import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    M, N, H = map(int, input().split())
    tomatoes = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
    days = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    q = deque()
    result = 0

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 1:
                    q.append((h,n,m,0))
    if len(q) == H*N*M:
        print(0)
        return
    while q:
        x, y, z, dep = q.popleft()
        for dx, dy, dz in d:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0 > nx or nx >= H or 0 > ny or ny >= N or 0 > nz or nz >= M:
                continue
            if tomatoes[nx][ny][nz] == 0:
                tomatoes[nx][ny][nz] = 1
                q.append((nx, ny, nz, dep + 1))
        result = max(result, dep)

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 0:
                    print(-1)
                    return

    print(result)


if __name__ == '__main__':
    solution()
