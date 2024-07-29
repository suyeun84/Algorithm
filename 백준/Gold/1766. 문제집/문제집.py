import sys
import heapq

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    degree = [0]*(N+1)
    answer = []
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1

    def check():
        heap = []
        for i in range(1, N+1):
            if degree[i] == 0:
                heapq.heappush(heap, i)
        while heap:
            curr = heapq.heappop(heap)
            answer.append(curr)
            for g in graph[curr]:
                degree[g] -= 1
                if degree[g] == 0:
                    heapq.heappush(heap, g)

    check()
    print(*answer)

if __name__ == '__main__':
    solution()