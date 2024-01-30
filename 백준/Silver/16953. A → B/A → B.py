import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
flag = True

def dfs(curr, cnt):
    global flag
    if curr == B:
        flag = False
        print(cnt+1)
        return
    elif curr>B:
        return
    else:
        if curr*2 <= B:
            dfs(curr*2, cnt+1)
        num = int(str(curr)+"1")
        if num <= B:
            dfs(num, cnt+1)

dfs(A, 0)
if flag: print(-1)