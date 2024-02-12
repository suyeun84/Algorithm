import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    dp = [[0 for _ in range(n)] for _ in range(2)]
    result = 0
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n == 1:
        result = max(dp[0][0], dp[1][0])
    if n >= 2:
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]
        result = max(dp[0][1], dp[1][1])
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1]+sticker[0][i], dp[0][i-2]+sticker[0][i], 
                       dp[1][i-2]+sticker[0][i], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1]+sticker[1][i], dp[0][i-2]+sticker[1][i], 
                       dp[1][i-2]+sticker[1][i], dp[1][i-1])
        if dp[0][i] > result:
            result = dp[0][i]
        if dp[1][i] > result:
            result = dp[1][i]
    print(result)