import sys
import heapq

def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, v = map(int, input().split())
        graph[s].append((v, e))

    start, target = map(int, input().split())

    def dijkstra():
        price = [int(1e9)] * (n+1)
        heap = []
        price[start] = 0

        heapq.heappush(heap, (0, start, [start]))
        
        while heap:
            curr_price, curr_city, curr_path = heapq.heappop(heap)
            if curr_city == target:
                print(curr_price)
                print(len(curr_path))
                print(*curr_path)
                break
            for v,e in graph[curr_city]:
                if price[e] <= curr_price + v:
                    continue
                price[e] = curr_price + v
                next_path = curr_path + [e]
                heapq.heappush(heap, (price[curr_city] + v, e, next_path))

    dijkstra()


if __name__ == '__main__':
    solution()