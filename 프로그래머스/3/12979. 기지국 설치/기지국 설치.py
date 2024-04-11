import math

def solution(n, stations, w):
    answer = 0
    w_range = 2*w+1
    start = 1
    for station in stations:
        end = station - w
        answer += math.ceil((end-start) / w_range)
        start = station + w + 1
        
    if start <= n:
        answer += math.ceil((n+1-start) / w_range)
    
    return answer