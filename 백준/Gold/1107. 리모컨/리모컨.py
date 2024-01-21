import sys
input = sys.stdin.readline
N = int(input()) # 이동하려는 채널
M = int(input()) # 고장난 버튼 수
broken = list(map(int, input().split()))
result = abs(100-N)

for nums in range(1000001):
    nums = str(nums)
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums)-1:
            result = min(result, len(nums)+abs(N-int(nums)))
    
print(result)