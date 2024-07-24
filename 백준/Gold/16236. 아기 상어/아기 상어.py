import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N = int(input())
    board = []
    curr_size = 2
    cnt = 0
    answer = 0
    d = [(-1,0), (0,-1), (0,1), (1,0)]
    for _ in range(N):
        board.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                cy, cx = i, j

    def bfs():
        nonlocal board, cnt, curr_size, cy, cx, answer
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[cy][cx] = 1
        board[cy][cx] = 0
        q = deque()
        possible_fish = []
        q.append((cy, cx, 0))
        while q:
            y, x, move = q.popleft()
            for dy, dx in d:
                ny = dy + y
                nx = dx + x
                if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0 and board[ny][nx] <= curr_size:
                    visited[ny][nx] = 1
                    if board[ny][nx] == curr_size or board[ny][nx] == 0:
                        # 지나만 감
                        q.append((ny, nx, move+1))
                        continue
                    # 잡아먹는 애들 중에 가장 위왼 골라야 함
                    elif board[ny][nx] < curr_size:
                        possible_fish.append((move+1, ny, nx))
        if possible_fish:
            possible_fish.sort()
            move, y, x = possible_fish[0]
            board[y][x] = 0
            cnt += 1
            if cnt == curr_size:
                curr_size += 1
                cnt = 0
            cy = y
            cx = x
            answer += move
            return False
        return True
                    
    while True:
        if bfs():
            print(answer)
            break


if __name__ == '__main__':
    solution()