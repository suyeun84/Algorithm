import sys
from collections import deque
from itertools import combinations
import copy


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    virus = []
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0

    for _ in range(N):
        virus.append(list(map(int, input().strip().split())))

    def bfs(tmp_virus):
        nonlocal answer
        q = deque()

        for i in range(N):
            for j in range(M):
                if tmp_virus[i][j] == 2:
                    q.append((i, j))

        while q:
            y, x = q.popleft()
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if 0 > ny or ny >= N or nx < 0 or nx >= M:
                    continue
                if tmp_virus[ny][nx] == 0:
                    tmp_virus[ny][nx] = 2
                    q.append((ny, nx))

        cnt = 0
        for i in range(N):
            for j in range(M):
                if tmp_virus[i][j] == 0:
                    cnt += 1
        answer = max(answer, cnt)

    def make_wall():
        com = []
        for i in range(N):
            for j in range(M):
                com.append([i,j])
        for li in combinations(com, 3):
            tmp_virus = copy.deepcopy(virus)
            flag = True
            for l in li:
                if tmp_virus[l[0]][l[1]] == 0:
                    tmp_virus[l[0]][l[1]] = 1
                else:
                    flag = False
                    break
            if flag:
                bfs(tmp_virus)
    make_wall()
    print(answer)


if __name__ == '__main__':
    solution()
