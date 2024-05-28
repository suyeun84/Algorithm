import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = []
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        r, c = map(int, input().split())
        nums.append((r, c))

    for L in range(1, N):
        for start in range(0, N - L):
            end = L + start
            dp[start][end] = int(1e9)

            for i in range(start, start + L):
                dp[start][end] = min(dp[start][end],
                                     dp[start][i] + dp[i + 1][end] + nums[start][0] * nums[i][1] * nums[end][1])

    print(dp[0][N - 1])


if __name__ == '__main__':
    solution()
