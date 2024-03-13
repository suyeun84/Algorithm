import heapq
def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, ((-1)*work, work))
    print(heap)
    while n > 0:
        mcnt, cnt = heapq.heappop(heap) #최대값 pop
        if cnt == 0:
            break
        heapq.heappush(heap, ((-1)*(cnt-1),cnt-1))
        n -= 1
    
    while heap:
        mcnt, cnt = heapq.heappop(heap)
        answer += cnt*cnt
    
    return answer