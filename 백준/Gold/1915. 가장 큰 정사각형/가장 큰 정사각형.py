import sys


def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0

    for i in range(n):
        nums = list(map(int, input().strip()))
        for j in range(m):
            dp[i][j] = nums[j]
            if nums[j] == 1 and i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + nums[j]
            answer = max(answer, dp[i][j])
    print(answer*answer)


if __name__ == '__main__':
    solution()
