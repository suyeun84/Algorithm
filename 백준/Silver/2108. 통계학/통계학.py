import sys
input = sys.stdin.readline
n = int(input().strip())
nums = []
#산술평균
avg = 0
for i in range(n):
    nums.append(int(input().strip()))
    avg += nums[i]
print(round(avg / n))
#중앙값
nums.sort()
print(nums[n//2])
#최빈값
dic = {}
for num in nums:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
cnt_most = []
most = 0
for key in dic.keys():
    if dic[key] > most:
        most = dic[key]
        cnt_most.clear()
        cnt_most.append(key)
    elif dic[key] == most:
        cnt_most.append(key)
if len(cnt_most) == 1:
    print(cnt_most[0])
elif len(cnt_most) > 1:
    cnt_most.sort()
    print(cnt_most[1])
#범위
print(max(nums)-min(nums))