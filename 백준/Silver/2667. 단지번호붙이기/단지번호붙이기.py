import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
array = []
cnt = []

for _ in range(N):
    array.append(list(map(int, input().strip())))

d = [[1,0], [0,1], [-1,0], [0,-1]]

def bfs(y,x):
    dq = deque()
    dq.append((y,x))
    array[y][x] = 0
    num = 1
    while dq:
        y1, x1 = dq.popleft()
        for dx, dy in d:
            if 0<=y1+dy<N and 0<=x1+dx<N:
                if array[y1+dy][x1+dx] == 1:
                    array[y1+dy][x1+dx] = 0
                    num += 1
                    dq.append((y1+dy, x1+dx))
    return num

for y in range(N):
    for x in range(N):
        if array[y][x] == 1:
            cnt.append(bfs(y,x))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])