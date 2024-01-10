from collections import deque

#동일 시간 내에서 가장 먼저 도착하는 경우
def bfs(n, k):
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        if n == k:
            print(graph[n])
            return
        for next_n in (n+1,n-1,n*2):
            if 0<=next_n<=100000:
                if graph[next_n]==0 or graph[next_n] > graph[n]+1:
                    graph[next_n] = graph[n] + 1
                    q.append(next_n)

n, k = map(int,input().split())
graph=[0]*100001
bfs(n,k)