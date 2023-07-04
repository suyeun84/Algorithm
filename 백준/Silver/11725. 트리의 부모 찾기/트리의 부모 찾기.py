#BFS
import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque()
queue.append(1)
while queue:
    node = queue.pop()
    for i in tree[node]:
        if result[i] == 0:
            result[i] = node
            queue.append(i)
for i in range(2, n+1):
    print(result[i])