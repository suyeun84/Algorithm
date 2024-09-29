import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    S = input().strip()
    T = input().strip()
    answer = 0

    q = deque()
    q.append(T)
    while q:
        t = q.popleft()
        if t == S:
            answer = 1
            break
        if len(t) <= len(S):
            continue
        if t[0] == 'B':
            q.append(t[1:][::-1])
        if t[-1] == 'A':
            q.append(t[:-1])
    print(answer)


if __name__ == '__main__':
    solution()
