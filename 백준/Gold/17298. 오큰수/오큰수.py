import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    answer = [-1]*N
    stack = [[nums[0], 0]]
    for i in range(1, N):
        while stack and nums[i] > stack[-1][0]:
            num, idx = stack.pop()
            answer[idx] = nums[i]
        stack.append([nums[i], i])
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    solution()
