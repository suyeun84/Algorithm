import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_value = max(map(max, board))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    d = [[1,0], [-1,0], [0,1], [0,-1]]

    def dfs(y, x, cnt, sum):
        nonlocal answer
        if 0 > y or y >= N or x < 0 or x >= M:
            return
        if cnt == 4:
            answer = max(answer, sum)
            return
        if sum + max_value*(4-cnt) <= answer:
            return
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                if cnt == 2:
                    visited[ny][nx] = 1
                    dfs(y, x, cnt + 1, sum+board[ny][nx])
                    visited[ny][nx] = 0
                visited[ny][nx] = 1
                dfs(ny, nx, cnt + 1, sum + board[ny][nx])
                visited[ny][nx] = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs(i, j, 1, board[i][j])
            visited[i][j] = 0

    print(answer)


if __name__ == '__main__':
    solution()
