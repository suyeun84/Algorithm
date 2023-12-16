import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())
maze = []

for _ in range(N):
    maze.append(list(map(int, input().strip())))

d = [[1,0], [0,1], [-1,0], [0,-1]]

def bfs(y,x):
    dq = deque()
    dq.append((y,x))
    while dq:
        y1, x1 = dq.popleft()
        for dx, dy in d:
            if 0<=y1+dy<N and 0<=x1+dx<M:
                if maze[y1+dy][x1+dx]==1:
                    maze[y1+dy][x1+dx] = maze[y1][x1]+1
                    dq.append((y1+dy, x1+dx))
                    
bfs(0,0)
print(maze[N-1][M-1])