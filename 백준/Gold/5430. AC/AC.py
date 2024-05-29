import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        p = list(input())
        n = int(input())
        result = []
        num = input().strip()
        nums = deque(num[1:len(num)-1].split(','))
        isReverse = False

        cnt = 0
        for ex in p:
            if ex == "D":
                cnt += 1
        if cnt > n:
            print('error')
            continue
        elif cnt == n:
            print(result)
            continue

        for lan in p:
            if lan == "D":
                if isReverse:
                    nums.pop()
                else:
                    nums.popleft()
                n -= 1
            elif lan == "R":
                if n < 2:
                    continue
                isReverse = not isReverse

        while n > 0:
            if isReverse:
                a = nums.pop()
                result.append(int(a))
            else:
                a = nums.popleft()
                result.append(int(a))
            n -= 1
        print("["+",".join(map(str,result))+"]")


if __name__ == '__main__':
    solution()