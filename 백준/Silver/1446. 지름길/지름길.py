import sys

input = sys.stdin.readline
N, D = map(int, input().split())
distance = [i for i in range(D+1)]
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split(' '))))

for i in range(D+1):
    distance[i] = min(distance[i], distance[i-1]+1)
    for start, end, dist in graph:
        if i == start and end <= D and distance[i] + dist < distance[end]:
            distance[end] = distance[start] + dist
    
print(distance[D])