import sys

input = sys.stdin.readline
N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
count = [[0]*N for _ in range(N)]
count[0][0] = 1

for x in range(N):
    for y in range(N):
        if game[x][y] != 0 and count[x][y] != 0:
            if x+game[x][y] < N:
                count[x+game[x][y]][y] += count[x][y]
            if y+game[x][y] < N:
                count[x][y+game[x][y]] += count[x][y]
print(count[N-1][N-1])