from collections import deque

def solution():
    n = int(input())

    q = deque()
    for i in range(1, n+1):
        q.append(i)
    for _ in range(n-1):
        q.popleft()
        num = q.popleft()
        q.append(num)
    print(*q)
    
if __name__ == '__main__':
    solution()
    