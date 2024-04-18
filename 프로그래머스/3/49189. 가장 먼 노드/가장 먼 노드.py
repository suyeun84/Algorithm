from collections import deque
def solution(n, vertex):
    answer = 0
    graph = [[]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)
    cnt = [0]*(n+1)
    idx = 0
    
    for v in vertex:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
        
    q = deque()
    q.append((1,0))
    visited[1] = 1
    while q:
        v, d = q.popleft()
        cnt[d] += 1
        idx = d
        for g in graph[v]:
            if visited[g] == 0:
                visited[g] = 1
                q.append((g, d+1))
    
    return cnt[idx]