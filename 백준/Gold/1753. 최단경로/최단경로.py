import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# V=정점 개수, E=간선개수
V, E = map(int, input().split())
# K=시작 정점 번호
K = int(input())

graph = [[] * (V+1) for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
    # u -> v 가중치w
    u, v, w = map(int, input().split())
    #graph[u][v] = min(graph[u-1][v-1], w)
    graph[u].append((v, w))

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        dist, curr_node = heapq.heappop(heap)
        if distance[curr_node] < dist:
            continue
        for i in graph[curr_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
        
dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])