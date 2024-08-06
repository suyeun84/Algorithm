import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    in_str = list(input().strip())
    target = list(input().strip())
    q = deque()
    answer = ''

    for i in range(len(in_str)):
        q.append(in_str[i])
        flag = True
        if len(q) >= len(target):
            for j in range(0, len(target)):
                if q[len(q)-j-1] == target[len(target)-j-1]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                for j in range(len(target)):
                    q.pop()
    if q:
        while q:
            answer += q.popleft()
    else:
        print('FRULA')

    print(answer)


if __name__ == '__main__':
    solution()