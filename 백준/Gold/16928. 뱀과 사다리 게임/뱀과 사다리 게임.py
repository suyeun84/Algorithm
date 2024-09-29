import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    up = {}
    down = {}
    for _ in range(N):
        x, y = map(int, input().split())
        up[x] = y
    for _ in range(M):
        u, v = map(int, input().split())
        down[u] = v

    def bfs():
        visited = [0]*101
        q = deque()
        q.append((1, 0))
        while q:
            curr, cnt = q.popleft()
            if curr == 100:
                print(cnt)
                return
            for i in range(1, 7):
                move = curr + i
                if move > 100 or visited[move] == 1:
                    continue
                visited[move] = 1
                if move in up:
                    move = up[move]
                    visited[move] = 1
                elif move in down:
                    move = down[move]
                    visited[move] = 1
                q.append((move, cnt + 1))

    bfs()


if __name__ == '__main__':
    solution()
