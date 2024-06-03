import sys
import heapq

def solution():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    K = int(input())
    INF = int(1e9)
    graph = [[] for _ in range(V+1)]
    distance = [INF for _ in range(V+1)]

    for _ in range(E):
        u1, v1, w1 = map(int, input().split())
        graph[u1].append((w1, v1))

    def dijkstra(start):
        nonlocal distance
        distance[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            curr_distance, node = heapq.heappop(heap)
            if curr_distance > distance[node]:
                continue
            for dist, end in graph[node]:
                if curr_distance + dist >= distance[end]:
                    continue
                distance[end] = curr_distance + dist
                heapq.heappush(heap, (distance[end], end))

    dijkstra(K)

    for i in range(1,V+1):
        if i == K:
            print(0)
            continue
        if distance[i] == INF:
            print("INF")
            continue
        print(distance[i])


if __name__ == '__main__':
    solution()
