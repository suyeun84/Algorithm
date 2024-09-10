import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(1000000)
    n = int(input())
    board = []
    d = [[1,0], [0,1], [-1,0], [0,-1]]
    answer = 1
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        board.append(list(map(int, input().split())))

    def dfs(y, x):
        if dp[y][x] != 0:
            return dp[y][x]
        dp[y][x] = 1
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n and board[y][x] < board[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx)+1)
        return dp[y][x]

    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                dfs(i, j)

    for i in range(n):
        answer = max(answer, max(dp[i]))
    print(answer)


if __name__ == '__main__':
    solution()
