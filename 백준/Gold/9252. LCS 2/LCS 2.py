import sys


def solution():
    input = sys.stdin.readline
    A = list(map(str, input().strip()))
    B = list(map(str, input().strip()))
    dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if A[j - 1] == B[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[-1][-1])

    path = []
    r = len(B)
    c = len(A)

    while r != 0 and c != 0:
        if A[c - 1] == B[r - 1]:
            path.append(A[c - 1])
            r = r - 1
            c = c - 1
        else:
            if dp[r][c - 1] > dp[r - 1][c]:
                c = c - 1
            else:
                r = r - 1
    while path:
        print(path.pop(), end='')


if __name__ == '__main__':
    solution()
