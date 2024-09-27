import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    def bfs(n, k):
        q = deque()
        q.append(n)
        visited[n] = 1
        while q:
            idx = q.popleft()
            if idx == k:
                return
            for nx in (2 * idx, idx - 1, idx + 1):
                if nx < 0 or nx > 100000:
                    continue
                if visited[nx]:
                    continue
                if nx == 2 * idx:
                    visited[nx] = visited[idx]
                else:
                    visited[nx] = visited[idx] + 1

                q.append(nx)

    visited = [0] * 100001
    bfs(N, K)
    print(visited[K]-1)


if __name__ == '__main__':
    solution()
