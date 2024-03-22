import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
INF = 1e9
dp = [INF for _ in range(n + 1)]

for i in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
start, target = map(int, input().split())
def dijkstra(x):
    dp[x] = 0
    heap = []
    heappush(heap, [0, x])
    while heap:
        cost, point = heappop(heap)
        if dp[point] < cost:
            continue
        for t, v in graph[point]:
            new_cost = cost + v
            if dp[t] > new_cost:
                dp[t] = new_cost
                heappush(heap, [new_cost, t])

dijkstra(start)
print(dp[target])