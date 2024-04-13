def solution(stones, k):
    start, end = 1, max(stones)
    
    while start <= end:
        print(start, end)
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
            elif stone >= mid:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
    
    return end