import sys
input = sys.stdin.readline

n = int(input())
glass = [int(input()) for _ in range(n)]
dp = [0]*n

dp[0] = glass[0]

for i in range(1, n):
    if i == 1:
        dp[1] = glass[0]+glass[1]
    elif i == 2:
        dp[2] = max(dp[1], dp[0]+glass[2], glass[1]+glass[2])
    else:
        dp[i] = max(dp[i-1], dp[i-3]+glass[i-1]+glass[i], dp[i-2]+glass[i])
        
print(dp[n-1])