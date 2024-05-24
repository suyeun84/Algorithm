import sys


# 삼성 기출 문제
def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    d = [[1,0], [-1,0], [0,1], [0,-1]]
    for _ in range(N):
        board.append(list(map(int, input().split())))

    def dfs(y, x, cnt, sum):
        nonlocal answer
        if 0 > y or y >= N or x < 0 or x >= M:
            return
        if cnt == 4:
            answer = max(answer, sum)
            return
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dfs(ny, nx, cnt + 1, sum + board[ny][nx])
                visited[ny][nx] = 0

    #ㅗ모양
    def t_shape(y, x, sum):
        nonlocal answer
        #가로
        if x+2 < M:
            if y-1 >= 0:
                total = sum
                total += (board[y][x+1] + board[y][x+2] + board[y-1][x+1])
                answer = max(answer, total)
            if y+1 < N:
                total = sum
                total += (board[y][x + 1] + board[y][x + 2] + board[y + 1][x + 1])
                answer = max(answer, total)
        #세로
        if y+2 < N:
            if x-1 >= 0:
                total = sum
                total += (board[y+1][x] + board[y+2][x] + board[y+1][x-1])
                answer = max(answer, total)
            if x+1 < M:
                total = sum
                total += (board[y+1][x] + board[y+2][x] + board[y+1][x+1])
                answer = max(answer, total)


    for i in range(N):
        for j in range(M):
            #box의 시작점 설정
            visited[i][j] = 1
            dfs(i, j, 1, board[i][j])
            visited[i][j] = 0
            t_shape(i, j, board[i][j])

    print(answer)


if __name__ == '__main__':
    solution()
