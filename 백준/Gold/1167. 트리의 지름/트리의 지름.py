import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    answer = 0
    max = 1
    V = int(input())
    tree = [[] for _ in range(V + 1)]
    for _ in range(V):
        lst = list(map(int, input().split()))
        node = lst[0]
        for i in range(1, len(lst) - 1, 2):
            tree[node].append((lst[i], lst[i + 1]))

    def bfs(start):
        nonlocal answer
        nonlocal max
        q = deque()
        q.append((start, 0))
        visited = [0] * (V + 1)
        visited[start] = 1
        while q:
            nod, dist = q.popleft()
            for n, d in tree[nod]:
                if visited[n] == 0:
                    visited[n] = 1
                    dis = dist + d
                    q.append((n, dis))
                    if dis > answer:
                        answer = dis
                        max = n

    bfs(1)
    bfs(max)
    
    print(answer)


if __name__ == '__main__':
    solution()
