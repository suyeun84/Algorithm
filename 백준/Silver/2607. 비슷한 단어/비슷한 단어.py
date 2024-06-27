import sys
import copy


def solution():
    input = sys.stdin.readline
    N = int(input())
    result = 0
    target = list(map(str, input().strip()))
    for i in range(N-1):
        check = list(map(str, input().strip()))
        target2 = copy.deepcopy(target)
        check2 = copy.deepcopy(check)
        for j in target:
            if j in check:
                check.remove(j)
                target2.remove(j)
        if len(check) <= 1 and len(target2) <= 1:
            result += 1
        
    print(result)


if __name__ == '__main__':
    solution()