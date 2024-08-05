import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    d = [[1,0], [-1,0], [0,1], [0,-1]]
    board = []
    q = deque()
    fire = deque()
    answer = 0

    R, C = map(int, input().split())
    visited = [[0 for _ in range(C)] for _ in range(R)]
    fire_cnt = [[int(1e9) for _ in range(C)] for _ in range(R)]


    curr_J = [0,0]

    for _ in range(R):
        board.append(input().strip())

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'J':
                q.append([i,j,1])
                visited[i][j] = 1
            elif board[i][j] == 'F':
                fire.append([i,j,1])
                fire_cnt[i][j] = 1
            elif board[i][j] == '#':
                visited[i][j] = 1
    
    def init_fire():
        nonlocal fire
        nonlocal fire_cnt
        
        while fire:
            # fire
            y, x, cnt = fire.popleft()
            for dy, dx in d:
                ny = y+dy
                nx = x+dx
                if 0>ny or ny>=R or 0>nx or nx>=C:
                    continue
                if board[ny][nx] == '#' or fire_cnt[ny][nx] <= cnt+1:
                    continue
                fire_cnt[ny][nx] = cnt+1
                fire.append([ny, nx, cnt+1])
            
    def get_out():
        nonlocal q
        nonlocal visited
        nonlocal fire_cnt
        nonlocal answer
        nonlocal board

        while q:
            y, x, cnt = q.popleft()
            if y==0 or y==R-1 or x==0 or x==C-1:
                answer = cnt
                return True
            for dy, dx in d:
                ny = y+dy
                nx = x+dx
                if 0>ny or ny>=R or 0>nx or nx>=C:
                    continue
                if board[ny][nx] == '#' or visited[ny][nx] == 1 or fire_cnt[ny][nx] <= cnt+1:
                    continue
                visited[ny][nx] = 1
                q.append([ny, nx, cnt+1])
        return False

    init_fire()

    if get_out():
        print(answer)
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    solution()