import sys
import heapq

def solution():
    input = sys.stdin.readline
    N = int(input())
    min_heap = [] #큰 순서로 나열
    max_heap = [] #작은 순서로 나열
    answer = []

    if N == 1:
        print(int(input()))
        return
    else:
        num = int(input())
        answer.append(num)
        heapq.heappush(max_heap, num)

    for i in range(1,N):
        target = int(input())
        if target > max_heap[0]:
            heapq.heappush(max_heap, target)
        elif target <= max_heap[0]:
            heapq.heappush(min_heap, -1*target)
        
        if len(max_heap) - len(min_heap) == 2:
            num = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -1*num)
        if len(min_heap) - len(max_heap) == 2:
            num = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -1*num)

        if i % 2 == 1:
            answer.append(-1 * min_heap[0])
        else:
            if len(max_heap) > len(min_heap):
                answer.append(max_heap[0])
            else:
                answer.append(-1*min_heap[0])

    for i in range(N):
        print(answer[i])


if __name__ == '__main__':
    solution()
