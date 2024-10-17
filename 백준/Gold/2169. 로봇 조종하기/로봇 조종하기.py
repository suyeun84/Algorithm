import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = []
    dp = [[-1e9 for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        board.append(list(map(int, input().split())))
    dp[0][0] = board[0][0]
    for i in range(1, M):
        dp[0][i] = dp[0][i-1] + board[0][i]

    for i in range(1, N):
        # 왼 -> 오
        left_to_right = [-1e9]*M
        for j in range(M):
            if j == 0:
                left_to_right[j] = board[i][j] + dp[i-1][j]
            else:
                left_to_right[j] = max(dp[i-1][j], left_to_right[j-1]) + board[i][j]
        # 오 -> 왼
        right_to_left = [-1e9]*M
        for j in range(M-1, -1, -1):
            if j == M-1:
                right_to_left[j] = dp[i-1][j] + board[i][j]
            else:
                right_to_left[j] = max(dp[i-1][j], right_to_left[j+1]) + board[i][j]
        for j in range(M):
            dp[i][j] = max(left_to_right[j], right_to_left[j])

    print(dp[N-1][M-1])


if __name__ == '__main__':
    solution()
