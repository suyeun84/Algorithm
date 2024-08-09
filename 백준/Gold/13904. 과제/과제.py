import sys
import heapq

def solution():
    input = sys.stdin.readline
    N = int(input())
    heap = []
    curr_day = 0
    answer = 0
    for _ in range(N):
        d, v = map(int, input().split())
        if d > curr_day:
            curr_day = d
        heapq.heappush(heap, (-1*d,-1*v))

    while curr_day >= 1 and heap:
        d, v = heapq.heappop(heap)
        end_day = -1 * d
        val = -1 * v
        if end_day > curr_day:
            heapq.heappush(heap,(-1*curr_day, v))
        elif end_day == curr_day:
            answer += val
            curr_day -= 1
        else:
            curr_day = end_day -1
            answer += val
    print(answer)


if __name__ == '__main__':
    solution()
