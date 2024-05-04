import sys
import heapq


def solution():
    input = sys.stdin.readline
    N = int(input())
    heap = []
    answer = 0
    for _ in range(N):
        heapq.heappush(heap, int(input()))

    if N == 1:
        print(0)
        return

    while heap:
        if len(heap) == 1:
            break
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b)
        answer += (a+b)

    print(answer)


if __name__ == '__main__':
    solution()
