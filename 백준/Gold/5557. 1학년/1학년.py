import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().strip().split(' ')))
    dp = [[0]*21 for _ in range(N)]
    dp[0][nums[0]] = 1
    for i in range(1, N-1):
        for j in range(21):
            if 0 <= j-nums[i] <= 20:
                dp[i][j] += dp[i-1][j-nums[i]]
            if 0 <= j+nums[i] <= 20:
                dp[i][j] += dp[i-1][j+nums[i]]

    print(dp[N-2][nums[-1]])


if __name__ == '__main__':
    solution()
