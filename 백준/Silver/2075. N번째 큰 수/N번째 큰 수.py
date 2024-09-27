import sys
import heapq

def solution():
    input = sys.stdin.readline
    N = int(input())
    heap = []
    for _ in range(N):
        nums = list(map(int, input().split()))
        for num in nums:
            if len(heap) == N:
                x = heapq.heappop(heap)
                heapq.heappush(heap, max(x, num))
            else:
                heapq.heappush(heap, num)

    print(heapq.heappop(heap))


if __name__ == '__main__':
    solution()
