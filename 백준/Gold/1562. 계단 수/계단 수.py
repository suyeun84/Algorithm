import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    answer = 0
    dp = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(N+1)]
    mod = 10**9

    for j in range(1, 10):
        dp[1][j][1<<j] = 1

    for i in range(1, N):
        for j in range(10):
            for b in range(1<<10):
                if j > 0:
                    next = b | 1<<(j-1)
                    dp[i+1][j-1][next] += dp[i][j][b]
                    dp[i+1][j-1][next] %= mod
                if j < 9:
                    next = b | 1<<(j+1)
                    dp[i+1][j+1][next] += dp[i][j][b]
                    dp[i+1][j+1][next] %= mod

    for i in range(10):
        answer += dp[N][i][(1<<10)-1]
        answer %= mod

    print(answer)

    
if __name__ == '__main__':
    solution()