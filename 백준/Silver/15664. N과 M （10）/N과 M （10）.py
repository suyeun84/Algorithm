import sys
input = sys.stdin.readline
def dfs(index):
    if len(s) == m:
        if tuple(s) not in result:
            result[tuple(s)] = 1
            print(*s)
        return
    for i in range(index, len(nums)):
        s.append(nums[i])
        dfs(i+1)
        s.pop()
            
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
result = {}

dfs(0)