import sys

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    start, end = 0, max(lst)

    while start <= end:
        sum = 0
        mid = (start + end) // 2

        for l in lst:
            if l > mid:
                sum += l - mid
        if sum >= m:
            start = mid + 1
        elif sum < m:
            end = mid - 1
    print(end)

if __name__ == '__main__':
    solution()
