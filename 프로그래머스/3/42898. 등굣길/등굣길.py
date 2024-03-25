def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
    dp[1][1] = 1
    
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1
        
    for i in range(2, n+1):
        if dp[i][1] == -1:
            continue
        if dp[i-1][1] == -1:
            dp[i][1] = 0
        else:
            dp[i][1] = dp[i-1][1]

    for j in range(2, m+1):
        if dp[1][j] == -1:
            continue
        if dp[1][j-1] == -1:
            dp[1][j] = 0
        else:
            dp[1][j] = dp[1][j-1]
            
    for i in range(2, n+1):
        for j in range(2, m+1):
            if dp[i][j] == -1:
                continue
            # puddle로 둘러쌓여 있는 경우
            if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                dp[i][j] == 0
                continue
            if dp[i-1][j] == -1:
                dp[i][j] = dp[i][j-1]
                continue
            if dp[i][j-1] == -1:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
                
    print(dp)
    return dp[n][m] % 1000000007