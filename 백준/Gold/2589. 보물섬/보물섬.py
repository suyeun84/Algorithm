import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
t = []
d = [[1,0], [-1,0], [0,1], [0,-1]]
result = 0
for _ in range(H):
    t.append(list(input()))

def bfs(i, j):
    cnt = 0
    q = deque()
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    q.append((i, j))
    visited[i][j] = 0
    while q:
        y, x = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<W and 0<=ny<H and t[ny][nx] == 'L' and visited[ny][nx] == -1:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
                cnt = max(cnt, visited[ny][nx])
    return cnt

for i in range(H):
    for j in range(W):
        if t[i][j] == 'L':
            result = max(result, bfs(i,j))
print(result)