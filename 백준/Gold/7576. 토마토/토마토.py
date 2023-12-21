import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
box = []
dq = deque()

for i in range(N):
    box.append(list(map(int, input().split())))

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            dq.append((y,x))
            
d = [[1,0], [0,1], [-1,0], [0,-1]]

def bfs():
    while dq:
        y1, x1 = dq.popleft()
        for dy, dx in d:
            if 0<=x1+dx<M and 0<=y1+dy<N:
                if box[y1+dy][x1+dx] == 0:
                    box[y1+dy][x1+dx] = box[y1][x1]+1
                    dq.append((y1+dy, x1+dx))

bfs()
day = 0
for row in box:
    if 0 in row:
        print(-1)
        exit()
    else:
        day = max(day, max(row))
print(day-1)