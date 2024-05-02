import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    mod = 1000000000

    for i in range(10):
        dp[1][i] = 1

    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1, 9):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
    sum = 0
    for i in range(1, 10):
        sum += dp[N][i] % mod
    print(sum % mod)


if __name__ == '__main__':
    solution()


