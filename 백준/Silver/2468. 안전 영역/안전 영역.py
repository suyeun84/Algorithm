import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
region = []
d = [[1,0], [-1,0], [0,1], [0,-1]]
result = 0
maxh = 0

for i in range(N):
    region.append(list(map(int, input().split())))
    for j in region[i]:
        maxh = max(maxh, j)
    

def bfs(y, x, h):
    q = deque()
    visited[y][x] = 1
    q.append((y,x))
    while q:
        y1, x1 = q.popleft()
        for dy, dx in d:
            ny = y1+dy
            nx = x1+dx
            if 0<=ny<N and 0<=nx<N and visited[ny][nx]==0 and region[ny][nx]>h:
                visited[ny][nx] = 1
                q.append((ny, nx))
    

for h in range(maxh):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and region[i][j]>h:
                bfs(i, j, h)
                count += 1
    result = max(result, count)
print(result)