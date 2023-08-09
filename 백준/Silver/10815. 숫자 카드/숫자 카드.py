import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().strip().split()))
m = int(input())
checks = list(map(int, input().strip().split()))
nums.sort()
#이분탐색
for check in checks:
    start, end = 0, n-1
    exist = False
    while start <= end:
        mid = (start + end) // 2
        if check == nums[mid]:
            exist = True
            break
        elif check < nums[mid]:
            end = mid - 1
        elif check > nums[mid]:
            start = mid + 1
    print(1 if exist else 0, end=' ')