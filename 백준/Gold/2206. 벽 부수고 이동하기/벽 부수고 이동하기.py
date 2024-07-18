import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = []
    d = [[1,0],[-1,0],[0,1],[0,-1]]
    answer = int(1e9)
    for _ in range(N):
        board.append(list(input().strip()))

    def bfs():
        nonlocal answer
        q = deque()
        visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
        #(y, x, 뚫은벽수, 현재까지거리)
        q.append((0,0,0,1))
        visited[0][0][0] = 1
        # 벽 뚫은거의 visited인지 벽 안뚫은거의 visited인지 구분 필요
        while q:
            y, x, cnt, ans = q.popleft()
            if y == N-1 and x == M-1:
                print(ans)
                exit()
            for dy, dx in d:
                ny = dy + y
                nx = dx + x
                if 0 > ny or ny >= N or 0 > nx or nx >= M:
                    continue
                if visited[ny][nx][cnt] == 1:
                    continue

                if int(board[ny][nx]) == 1 and cnt == 0:
                    visited[ny][nx][1] = 1
                    q.append((ny,nx,1,ans+1))
                    continue
                elif int(board[ny][nx]) == 0:
                    visited[ny][nx][cnt] = 1
                    q.append((ny,nx,cnt,ans+1))

    bfs()
    print(-1)


if __name__ == '__main__':
    solution()