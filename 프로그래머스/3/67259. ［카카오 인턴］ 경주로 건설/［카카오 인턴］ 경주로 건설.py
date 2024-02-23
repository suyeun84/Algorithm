from collections import deque
def solution(board):
    size = len(board)
    d = [[1,0], [-1,0], [0,1], [0,-1]]
    
    def bfs(start):
        price = [[1e9 for _ in range(size)] for _ in range(size)]
        price[0][0] = 0
        q = deque()
        q.append(start) #y, x, cost, dir
        while q:
            y, x, cost, direct = q.popleft()
            for dy, dx in d:
                ny = y+dy
                nx = x+dx
                if 0 <= ny < size and 0 <= nx < size and board[y][x] == 0:
                    if (dy != 0 and direct == 0) or (dx != 0 and direct == 1):
                        ncost = cost + 600
                    elif (dy != 0 and direct == 1) or (dx != 0 and direct == 0):
                        ncost = cost + 100
                        
                    if ncost < price[ny][nx]:
                        price[ny][nx] = ncost
                        if dy != 0:
                            q.append((ny, nx, ncost, 1))
                        else:
                            q.append((ny, nx, ncost, 0))
        return price[-1][-1]
                        
    #4번째 인자 0이면 x축이동, 1이면 y축이동
    return min(bfs((0, 0, 0, 1)), bfs((0, 0, 0, 0)))