import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
result = 0
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(curr):
    global result
    visited[curr] = 1
    for com in graph[curr]:
        if(visited[com] == 0):
            dfs(com)
            result += 1
        
dfs(1)
print(result)