def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0]
    
    dp = [0]*size
    
    dp[0] = sticker[0]
    dp[1] = max(sticker[0], sticker[1])
    
    for i in range(2, size-1):
        dp[i] = max(dp[i-1], dp[i-2]+sticker[i])
        
    dp2 = [0]*size
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    
    return max(dp[size-2], dp2[size-1])