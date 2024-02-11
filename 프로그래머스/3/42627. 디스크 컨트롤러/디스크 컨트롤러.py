import heapq
def solution(jobs):
    answer, curr, fin_job = 0, 0, 0
    start = -1
    heap = []
    jobs.sort()
    while fin_job < len(jobs):
        for job in jobs:
            if start < job[0] <= curr:
                heapq.heappush(heap, (job[1], job[0])) #(시작시간, 소요시간)
        if len(heap) == 0:
            curr += 1
            continue
        job = heapq.heappop(heap) #(소요시간, 시작시간)
        start = curr
        curr = curr + job[0]
        fin_job += 1
        answer += (curr-job[1])
            
    return answer // len(jobs)