import sys
from collections import deque
input = sys.stdin.readline
seat = [list(input()) for _ in range(5)]

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

#arr에 있는 좌표들이 인접해 있는지 확인
def bfs(arr):
    visited = [[1]*5 for _ in range(5)]
    q = deque()
    for a in arr:
        visited[a[0]][a[1]] = 0
    
    q.append((arr[0]))
    visited[arr[0][0]][arr[0][1]] = 1
    check = 1
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr = dr + r
            nc = dc + c
            if 0<=nr<5 and 0<=nc<5 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                check += 1
                q.append((nr, nc))
            
    if check == 7:
        return True
    return False


def dfs(depth, start, cnt): #cnt는 상대팀 인원 count
    global answer
    if cnt >= 4:
        return
    if depth == 7:
        #arr에 있는 좌표들이 인접해 있는지 확인
        if bfs(arr):
            answer += 1
        return
    
    for i in range(start, 25):
        r = i // 5
        c = i % 5
        arr.append((r,c))
        if seat[r][c] == 'S':
            dfs(depth+1, i+1, cnt)
        else:
            dfs(depth+1, i+1, cnt+1)
        arr.pop()

arr = []
answer = 0
dfs(0, 0, 0)
print(answer)