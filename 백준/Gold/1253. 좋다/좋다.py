import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    answer = 0
    for i in range(N):
        target = nums[i]
        s, e = 0, N-1
        while s < e:
            total = nums[s] + nums[e]
            if total < target:
                s += 1
            elif total > target:
                e -= 1
            else:
                if s != i and e != i:
                    answer += 1
                    break
                elif s == i:
                    s += 1
                elif e == i:
                    e -= 1

    print(answer)


if __name__ == '__main__':
    solution()
