import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    degree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    q = deque()
    answer = []

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        degree[B] += 1
    
    for idx in range(1, N+1):
        if degree[idx] == 0:
            q.append(idx)
    while q:
        idx = q.popleft()
        answer.append(idx)
        for g in graph[idx]:
            degree[g] -= 1
            if degree[g] == 0:
                q.append(g)

    print(*answer)


if __name__ == '__main__':
    solution()
