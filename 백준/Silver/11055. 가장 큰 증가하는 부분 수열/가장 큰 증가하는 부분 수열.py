import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().strip().split()))
dp = [0]*n
for i in range(n):
    dp[i] = nums[i]
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+nums[i])
print(max(dp))