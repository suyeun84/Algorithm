import sys


def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    country = []
    for _ in range(N):
        c, g, s, m = map(int, input().split())
        country.append([c, g, s, m])
    country.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    rank = 1
    for i in range(len(country)):
        if i == 0:
            if country[i][0] == K:
                print(1)
                break
            else:
                continue
        for j in range(1, 4):
            if country[i-1][j] != country[i][j]:
                rank = i+1
                break
        if country[i][0] == K:
            print(rank)
            break


if __name__ == '__main__':
    solution()
