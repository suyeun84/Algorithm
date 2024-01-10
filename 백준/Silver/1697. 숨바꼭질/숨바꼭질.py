from collections import deque
n, k = map(int,input().split())
graph=[0]*1000001
def bfs(n,k):
    q = deque()
    q.append(n)
    graph[n] = 1
    while q:
        n = q.popleft()
        if n == k:
            print(graph[n]-1)
            return
        for nn in (n+1,n-1,n*2):
            if 0<=nn<=100000:
                if not graph[nn] or graph[nn] > graph[n]+1:
                    graph[nn] = graph[n] + 1
                    q.append(nn)
bfs(n,k)