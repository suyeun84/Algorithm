import sys

def solution():
    input = sys.stdin.readline
    T = int(input())
    m = [0,0,1,7,4,2,0,8,10]
    dp = [0,0,1,7,4,2,6,8,10] + [sys.maxsize]*93
    for idx in range(9, 101):
        for j in range(2, 8):
            dp[idx] = min(dp[idx], dp[idx - j] * 10 + m[j])
    for _ in range(T):
        N = int(input())
        max_ans = ''
        if N % 2 == 0:
            max_ans = '1'*(N//2)
        else:
            max_ans = '7' + '1'*((N-3)//2)
        print(dp[N], max_ans)

if __name__ == '__main__':
    solution()
