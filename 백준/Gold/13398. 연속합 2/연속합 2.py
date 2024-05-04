import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    result = nums[0]

    L = [0]*N
    L[0] = nums[0]
    for i in range(1, N):
        L[i] = max(nums[i], L[i-1]+nums[i])
        result = max(result, L[i])

    R = [0]*N
    R[N-1] = nums[N-1]
    for i in range(N-2, -1, -1):
        R[i] = max(nums[i], R[i+1]+nums[i])

    # 삭제할 index 설정
    for idx in range(1, N-1):
        result = max(result, L[idx-1]+R[idx+1])

    print(result)


if __name__ == '__main__':
    solution()
