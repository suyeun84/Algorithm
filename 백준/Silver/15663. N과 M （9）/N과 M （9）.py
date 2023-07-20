import sys
input = sys.stdin.readline
def dfs():
    if len(s) == m:
        if tuple(s) not in result:
            result[tuple(s)] = 1
            print(*s)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        s.append(nums[i])
        dfs()
        s.pop()
        visited[i] = False
            
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
result = {}
visited= [False]*(n)

dfs()