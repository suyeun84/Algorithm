import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    region = list(map(int, input().strip().split(' ')))
    M = int(input())
    start = 0
    end = max(region)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in range(N):
            if region[i] <= mid:
                total += region[i]
            else:
                total += mid
        if total > M:
            end = mid - 1
        elif total == M:
            end = mid
            break
        else:
            start = mid + 1
    print(end)


if __name__ == '__main__':
    solution()
