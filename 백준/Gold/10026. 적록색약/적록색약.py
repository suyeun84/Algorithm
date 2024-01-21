import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
area = [list(map(str, input())) for _ in range(N)]
normal = 0
abnormal = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
d = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs(y, x):
    q = deque()
    visited[y][x] = 1
    q.append((y,x))
    while q:
        y1, x1 = q.popleft()
        for dy, dx in d:
            ny = y1+dy
            nx = x1+dx
            if 0<=ny<N and 0<=nx<N:
                if area[ny][nx] == area[y1][x1] and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
    

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j)
            normal += 1

for i in range(N):
    for j in range(N):
        if area[i][j] == "G":
            area[i][j] = "R"
            
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j)
            abnormal += 1
        
print(str(normal)+" "+str(abnormal))