import sys
import heapq


def solution():
    input = sys.stdin.readline
    N = int(input())
    minus_heap = []
    plus_heap = []
    answer = 0
    for _ in range(N):
        a = int(input())
        if a > 0:
            #큰수부터 출력
            heapq.heappush(plus_heap, (-a, a))
        else:
            heapq.heappush(minus_heap, a)

    while plus_heap:
        if len(plus_heap) == 1:
            x, y = heapq.heappop(plus_heap)
            answer += y
            break
        x1, y1 = heapq.heappop(plus_heap)
        x2, y2 = heapq.heappop(plus_heap)
        answer += max(y1+y2, y1*y2)

    while minus_heap:
        if len(minus_heap) == 1:
            x = heapq.heappop(minus_heap)
            answer += x
            break
        x1 = heapq.heappop(minus_heap)
        x2 = heapq.heappop(minus_heap)
        answer += (x1*x2)

    print(answer)


if __name__ == '__main__':
    solution()
