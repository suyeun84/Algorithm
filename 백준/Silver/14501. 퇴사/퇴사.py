import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    dp = [0]*(N+2)

    for i in range(1, N+1):
        T, P = map(int, input().split())
        dp[i] = max(dp[i], dp[i-1])
        if i + T > N+1:
            continue
        dp[i+T] = max(dp[i+T], dp[i] + P)
    print(max(dp))


if __name__ == '__main__':
    solution()
