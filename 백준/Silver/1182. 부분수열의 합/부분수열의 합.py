import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

def dfs(index, total):
    global result
    if total == s and index != 0:
        result += 1
    for i in range(index, len(nums)):
        dfs(i+1, total+nums[i])

dfs(0, 0)
print(result)