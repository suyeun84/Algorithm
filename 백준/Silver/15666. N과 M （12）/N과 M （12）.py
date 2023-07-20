import sys
input = sys.stdin.readline
def dfs():
    if len(s) == m:
        if tuple(s) not in result:
            result[tuple(s)] = 1
            print(*s)
        return
    for i in nums:
        if len(s) == 0 or i >= s[-1]:
            s.append(i)
            dfs()
            s.pop()
            
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
result = {}

dfs()