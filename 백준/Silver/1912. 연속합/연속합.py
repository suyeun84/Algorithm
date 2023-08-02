import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().strip().split()))
dp = [0]*n
result = -sys.maxsize-1
for i in range(0, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
print(max(dp))