import sys

def solution():
    input = sys.stdin.readline
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    curr, total, answer = 0, 0, N+1
    for i in range(N):
        total += nums[i]
        while total >= S:
            answer = min(answer, i - curr + 1)
            total -= nums[curr]
            curr += 1
    if answer == N+1:
        print(0)
    else:
        print(answer)


if __name__ == '__main__':
    solution()
