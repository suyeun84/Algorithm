import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = []
    answer = 0
    zero_cnt = 0
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for _ in range(r):
        board.append(list(map(int, input().split(' '))))

    for i in range(r):
        for j in range(c):
            if board[i][j] == 0:
                zero_cnt += 1

    def change():
        nonlocal zero_cnt
        change = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] == 0:
                    continue
                for dy, dx in d:
                    ny, nx = i + dy, j + dx
                    if 0 > ny or r <= ny or 0 > nx or c <= nx:
                        continue
                    if board[ny][nx] == 0 and change[ny][nx] == 0:
                        if board[i][j] - 1 > 0:
                            board[i][j] -= 1
                        elif board[i][j] - 1 == 0:
                            board[i][j] -= 1
                            zero_cnt += 1
                        change[i][j] = 1

    def check(i, j):
        nonlocal visited
        q = deque()
        q.append([i, j])
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 > ny or r <= ny or 0 > nx or c <= nx:
                    continue
                if board[ny][nx] != 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])

    while True:
        if zero_cnt == r*c:
            print(0)
            break
        visited = [[0 for _ in range(c)] for _ in range(r)]
        answer += 1
        change()
        cnt = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] != 0 and visited[i][j] == 0:
                    cnt += 1
                    if cnt >= 2:
                        print(answer)
                        return
                    check(i, j)


if __name__ == '__main__':
    solution()
    