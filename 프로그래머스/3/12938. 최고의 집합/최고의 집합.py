def solution(n, s):
    # 자연수 n개로 이루어진 합 s인 집합
    arr = []
    answer = 0
    result = [0]*n
    
    if s < n:
        return [-1]
    
    mid = s//n
    left = s%n
    for i in range(n):
        if left > 0:
            result[i] = mid + 1
            left -= 1
        else:
            result[i] = mid
    result.sort()
    return result