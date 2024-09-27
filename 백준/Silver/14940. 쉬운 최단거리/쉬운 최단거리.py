import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = []
    target = []
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    d = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(n):
        board.append(list(map(int, input().split())))
        for j in range(m):
            if board[i][j] == 2:
                target = [i, j]
            elif board[i][j] == 0:
                dist[i][j] = 0

    def bfs(ty, tx):
        nonlocal dist, board
        q = deque()
        q.append([ty, tx])
        dist[ty][tx] = 0
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                ny, nx = dy + y, dx + x
                if 0 > ny or ny >= n or nx < 0 or nx >= m or dist[ny][nx] != -1 or board[ny][nx] == 0:
                    continue
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny, nx])

    bfs(target[0], target[1])
    for i in range(n):
        print(*dist[i])


if __name__ == '__main__':
    solution()
