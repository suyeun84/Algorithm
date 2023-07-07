import sys
n, m, v = map(int, input().strip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
result = [v]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = graph[b][a] = 1

#visited = 1로 방문 표시
def dfs(curr):
    visited[curr] = 1
    for i in range(1, n+1):
        if graph[curr][i] == 1 and visited[i] == 0:
            result.append(i)
            dfs(i)
            
#vistied = 0으로 방문 표시
def bfs(curr):
    q = [curr]
    visited[curr] = 0
    while q:
        pos = q.pop(0)
        print(pos, end=" ")
        for i in range(1, n+1):
            if graph[pos][i] == 1 and visited[i] == 1:
                q.append(i)
                visited[i] = 0
    
dfs(v)
print(*result)
bfs(v)