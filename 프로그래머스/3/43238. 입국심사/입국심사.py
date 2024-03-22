def solution(n, times):    
    start, end = 0, max(times)*n
    answer = end
    
    while start <= end:
        mid = (start + end) // 2
        
        people = 0
        for time in times:
            people += mid // time
        
        if people >= n:
            end = mid - 1
            if answer > mid:
                answer = mid
            
        elif people < n:
            start = mid + 1
    
    return answer