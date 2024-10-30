import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    dic = {}
    answer, curr = 0, 0
    for i in range(N):
        if nums[i] in dic:
            while nums[curr] != nums[i]:
                dic.pop(nums[curr])
                curr += 1
            curr += 1
        dic[nums[i]] = 1
        answer += (i-curr+1)
    print(answer)


if __name__ == '__main__':
    solution()
