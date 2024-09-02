import sys
import heapq


def solution():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    heap = []
    visited = [0]*(N+1)
    answer = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([c, b])
        graph[b].append([c, a])

    heapq.heappush(heap, (0, 1))
    while heap:
        val, curr = heapq.heappop(heap)
        if visited[curr] == 0:
            visited[curr] = 1
            answer += val
            for dist, end in graph[curr]:
                if visited[end] == 0:
                    heapq.heappush(heap, (dist, end))

    print(answer)


if __name__ == '__main__':
    solution()
