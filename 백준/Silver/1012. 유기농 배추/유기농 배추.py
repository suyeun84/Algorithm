import sys
input = sys.stdin.readline

def dfs(y, x):
    stack = [[y,x]]
    while stack:
        i, j = stack.pop()
        ground[i][j] = 0
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M and ground[ni][nj] == 1:
                stack.append([ni,nj])


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    result = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                dfs(i, j)
                result += 1
    print(result)