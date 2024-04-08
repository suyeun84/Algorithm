import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = int(input())
    num = list(map(int, input().split()))

    def binary_search(target):
        start, end = 0, n-1

        while start <= end:
            if start > end:
                return 0

            mid = (start + end) // 2
            if a[mid] < target:
                start = mid + 1
            elif a[mid] > target:
                end = mid - 1
            else:
                return 1
        return 0

    for k in num:
        print(binary_search(k))


if __name__ == '__main__':
    solution()
