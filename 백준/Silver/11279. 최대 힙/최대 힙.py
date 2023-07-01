import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(heap, (-1)*num)
    else:
        if len(heap) > 0:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)