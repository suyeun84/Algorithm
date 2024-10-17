import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    N, L, R = map(int, input().split())
    board = []
    answer = 0
    d = [[1,0], [-1,0], [0,1], [0,-1]]
    for _ in range(N):
        board.append(list(map(int, input().split())))

    def search(y, x):
        q = deque()
        q.append((y, x))
        visited[y][x] = True
        union = [(y, x)]

        while q:
            y, x = q.popleft()
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if L <= abs(board[ny][nx] - board[y][x]) <= R:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                        union.append((ny, nx))
        return union

    while True:
        visited = [[False for _ in range(N)] for _ in range(N)]
        stop = True

        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    continue
                union = search(i, j)

                if len(union) > 1:
                    stop = False
                    total = 0
                    for y, x in union:
                        total += board[y][x]
                    num = total // len(union)
                    for y, x in union:
                        board[y][x] = num
        if stop:
            break
        answer += 1

    print(answer)


if __name__ == '__main__':
    solution()
