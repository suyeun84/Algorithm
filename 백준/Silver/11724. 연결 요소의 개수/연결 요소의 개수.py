import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[]for i in range(N+1)]
visited = [0] *(N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(curr):
    visited[curr] = 1
    q = deque()
    for u in graph[curr]:
        q.append(u)
        visited[u] = 1
    while q:
        k = q.popleft()
        for v in graph[k]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = 1
    
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)