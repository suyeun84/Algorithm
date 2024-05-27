import sys


def solution():
    input = sys.stdin.readline
    N, L, R = map(int, input().split())
    dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    dp[1][1][1] = 1

    for i in range(2, N+1):
        for j in range(1, L+1):
            for z in range(1, R+1):
                dp[i][j][z] = (dp[i-1][j-1][z] + dp[i-1][j][z-1] + dp[i-1][j][z] * (i-2)) % 1000000007

    print(dp[N][L][R])


if __name__ == '__main__':
    solution()
