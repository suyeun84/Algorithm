import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    cnt = 1

    def bfs(board, N):
        dp = [[1e9 for _ in range(N)] for _ in range(N)]
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        q.append([0,0])
        dp[0][0] = board[0][0]
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if 0 > ny or ny >= N or nx < 0 or nx >= N:
                    continue
                if dp[ny][nx] <= dp[y][x] + board[ny][nx]:
                    continue
                dp[ny][nx] = dp[y][x] + board[ny][nx]
                q.append([ny, nx])
        print("Problem " + str(cnt) + ": " + str(dp[N-1][N-1]))

    while True:
        N = int(input())
        if N == 0:
            break
        board = []
        for _ in range(N):
            board.append(list(map(int, input().split())))

        bfs(board, N)
        cnt += 1


if __name__ == '__main__':
    solution()
