import sys

def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10000)
    M, N = map(int, input().split())
    board = []
    dp = [[-1 for _ in range(N)] for _ in range(M)]
    d = [(1,0), (-1,0), (0,1), (0,-1)]
    for _ in range(M):
        board.append(list(map(int, input().split())))

    def dfs(y, x):
        nonlocal dp

        if y == M-1 and x == N-1:
            return 1
        
        if dp[y][x] != -1:
            return dp[y][x]
        ways = 0
        for dy, dx in d:
            ny = y+dy
            nx = x+dx
            if 0<=ny<M and 0<=nx<N:
                if board[y][x] > board[ny][nx]:
                    ways += dfs(ny, nx)
        dp[y][x] = ways
        return dp[y][x]

    print(dfs(0,0))     
            

if __name__ == '__main__':
    solution()