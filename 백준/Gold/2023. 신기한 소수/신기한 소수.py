import math
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = []
    can = [1,3,7,9]

    def check(num):
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
        return True

    nums.append([2,3,5,7])
    idx = 0
    while idx < N-1:
        l = []
        for i in nums[idx]:
            for j in can:
                tmp = str(i) + str(j)
                if check(int(tmp)):
                    l.append(int(tmp))
        idx += 1
        nums.append(l)

    for n in sorted(nums[N-1]):
        print(n)


if __name__ == '__main__':
    solution()
