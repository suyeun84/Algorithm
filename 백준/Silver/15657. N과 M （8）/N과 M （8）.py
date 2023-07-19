def dfs(prev):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in nums:
        if i >= prev:
            s.append(i)
            dfs(i)
            s.pop()
    
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
dfs(nums[0])