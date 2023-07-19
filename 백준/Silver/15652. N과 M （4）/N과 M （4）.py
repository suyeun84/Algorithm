def dfs(prev):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(prev, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
n, m = map(int, input().split())
s = []
dfs(1)