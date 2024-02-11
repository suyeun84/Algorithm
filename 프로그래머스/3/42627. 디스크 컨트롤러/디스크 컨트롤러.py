import heapq
def solution(jobs):
    start = -1
    answer, fin_job, curr = 0, 0, 0
    waiting = []
    jobs.sort()
    while fin_job < len(jobs):
        for job in jobs:
            if start < job[0] <= curr:
                heapq.heappush(waiting, (job[1], job[0])) #(소요시간, 시작시간)
        if len(waiting) == 0:
            curr += 1
            continue
        job = heapq.heappop(waiting)
        start = curr
        curr += job[0]
        answer += (curr - job[1])
        fin_job += 1
        
    return answer // len(jobs)