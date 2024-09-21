import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        name, val = map(str, input().strip().split(' '))
        arr.append([name, int(val)])
    for _ in range(M):
        num = int(input())
        start = 0
        end = len(arr)
        while start < end:
            mid = (start + end) // 2
            if arr[mid][1] >= num:
                end = mid
            else:
                start = mid + 1
        print(arr[end][0])


if __name__ == '__main__':
    solution()