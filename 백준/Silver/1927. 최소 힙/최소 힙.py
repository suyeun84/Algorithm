import sys
import heapq

def solution():
    input = sys.stdin.readline
    N = int(input())
    heap = []
    for _ in range(N):
        num = int(input())
        if num == 0:
            if len(heap) == 0:
                print(0)
                continue
            pop = heapq.heappop(heap)
            print(pop)
        else:
            heapq.heappush(heap, num)


if __name__ == '__main__':
    solution()
