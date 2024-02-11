import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)
        answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer