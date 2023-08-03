import sys
input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
stack = []
result = []
index = 0
for i in range(1, n+1):
    stack.append(i)
    result.append('+')
    while stack:
        if stack[-1] == nums[index]:
            index += 1
            stack.pop()
            result.append('-')
        else:
            break
if stack:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])