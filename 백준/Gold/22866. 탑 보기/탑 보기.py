import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    b = [0] + list(map(int, input().split()))
    answer = [[0, -int(1e9)] for _ in range(N+1)]
    # [보이는 건물 갯수, 최소 인덱스]
    left = []
    for i in range(1, N+1):
        while left and b[left[-1]] <= b[i]:
            left.pop()
        answer[i][0] += len(left)
        if left:
            answer[i][1] = left[-1]
        left.append(i)

    right = []
    for i in range(N, 0, -1):
        while right and b[right[-1]] <= b[i]:
            right.pop()
        answer[i][0] += len(right)
        if right and right[-1] - i < i - answer[i][1]:
            answer[i][1] = right[-1]
        right.append(i)

    for i in range(1, N + 1):
        if answer[i][0] != 0:
            print(answer[i][0], answer[i][1])
        else:
            print(0)


if __name__ == '__main__':
    solution()
