def dfs():
    if len(s) == m:
        if tuple(s) not in result:
            result[tuple(s)] = 1
            print(*s)
        return
    for i in nums:
        s.append(i)
        dfs()
        s.pop()
            
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
result = {}

dfs()