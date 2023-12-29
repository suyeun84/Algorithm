import sys

input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
result = sys.maxsize

def dfs(start, curr, val, cnt):
    global result
    #종료조건
    if val > result:
        return
    if cnt == N and W[curr][start] != 0:
        val += W[curr][start]
        if result > val:
            result = val
        return
    
    for i in range(N):
        if W[curr][i] != 0 and visited[i] == 0:
            visited[i] = 1
            dfs(start, i, val+W[curr][i], cnt+1)
            visited[i] = 0
    
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
    
print(result)