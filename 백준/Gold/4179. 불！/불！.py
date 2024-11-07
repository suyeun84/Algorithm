import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    board = []
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    jx, jy = 0, 0
    fire = [[1e9 for _ in range(C)] for _ in range(R)]
    point = []
    answer = 1e9
    for _ in range(R):
        board.append(input().strip())

    for i in range(R):
        for j in range(C):
            if board[i][j] == "F":
                point.append([i, j])
            if board[i][j] == "J":
                jx, jy = j, i

    def init_fire():
        nonlocal fire, point
        q = deque()
        for fy, fx in point:
            q.append([fy, fx])
            fire[fy][fx] = 1
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 > ny or ny >= R or nx < 0 or nx >= C:
                    continue
                if board[ny][nx] == "#" or fire[ny][nx] != 1e9:
                    continue
                fire[ny][nx] = fire[y][x] + 1
                q.append([ny, nx])

    def bfs():
        nonlocal answer
        visited = [[-1 for _ in range(C)] for _ in range(R)]
        q = deque()
        q.append([jy, jx])
        visited[jy][jx] = 1
        while q:
            y, x = q.popleft()
            if y == 0 or x == 0 or y == R-1 or x == C-1:
                answer = visited[y][x]
                return True
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 > ny or ny >= R or nx < 0 or nx >= C:
                    continue
                if board[ny][nx] == "#" or visited[ny][nx] != -1 or (fire[ny][nx] <= visited[y][x]+1):
                    continue
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])
        return False

    init_fire()
    if bfs():
        print(answer)
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    solution()
