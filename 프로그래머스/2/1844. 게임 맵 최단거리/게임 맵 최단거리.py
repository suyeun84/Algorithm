from collections import deque 
def solution(maps): 
    dx=[-1,1,0,0] 
    dy=[0,0,-1,1]

    def bfs (x,y):
        queue=deque()
        queue.append((x,y))
        while queue: 
            x,y=queue.popleft() 
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0>nx or 0>ny or nx>=len(maps) or ny>=len(maps[0]):
                    continue
                if maps[nx][ny]==0: 
                    continue
                if maps[nx][ny]==1: 
                    queue.append((nx,ny)) 
                    maps[nx][ny]=maps[x][y]+1  
    bfs(0,0)
    answer=maps[len(maps)-1][len(maps[0])-1]

    if answer==1: 
        answer=-1
    return answer