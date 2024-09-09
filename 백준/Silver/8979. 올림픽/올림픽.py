import sys

def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    country = []
    for _ in range(N):
        c, g, s, m = map(int, input().split())
        country.append([c,g,s,m])
    country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    rank = 1
    for i in range(len(country)-1):
        if country[i][0] == K:
            print(rank)
            break
        for j in range(1,4):
            if country[i][j] != country[i+1][j]:
                rank = i+2


if __name__ == '__main__':
    solution()
