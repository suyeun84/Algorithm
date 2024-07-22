import sys
import heapq

def solution():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    answer = 0
    # 양의 가중치만 주어지므로 다익스트라
    # 음의 가중치가 주어지면 벨만-포드 (N-1)번 실행

    def dijkstra(start, target):
        # X번 마을에서 파티하는데 가장 많은 시간 소요하는 학생의 시간 출력
        distance = [int(1e9)]*(N+1)
        heap = []
        for t, end in graph[start]:
            heapq.heappush(heap, (t,end))

        while heap:
            t, end = heapq.heappop(heap)
            if end == target:
                if distance[target] > t:
                    distance[target] = t
                    break
            if distance[end] > t:
                distance[end] = t
                for t1,end1 in graph[end]:
                    heapq.heappush(heap, (t1+distance[end], end1)) 
            
        return distance[target]

    for _ in range(M):
        start, end, T = map(int, input().strip().split())
        graph[start].append((T, end))

    for i in range(1, N+1):
        if i == X:
            continue
        dist = dijkstra(i, X) + dijkstra(X,i)
        if dist > answer:
            answer = dist
    print(answer)


if __name__ == '__main__':
    solution()
