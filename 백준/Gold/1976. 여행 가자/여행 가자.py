import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N = int(input()) # 도시의 수
    M = int(input()) # 여행 계획에 속한 도시들의 수
    board = []
    plan = []
    isConnected = [-1]*N
    for i in range(N):
        board.append(list(map(int, input().split())))
    plan = list(map(int, input().split()))

    def findPath(start):
        nonlocal isConnected
        q = deque()
        q.append(start)
        visited = [0]*N
        isConnected[start] = start
        visited[start] = 1
        while(q):
            curr = q.popleft()
            for i in range(N):
                if board[curr][i] == 1 and visited[i] == 0:
                    isConnected[i] = start
                    q.append(i)
                    visited[i] = 1

    for i in range(N):
        if isConnected[i] == -1:
            findPath(i)

    for i in range(1, M):
        if isConnected[plan[i-1]-1] == isConnected[plan[i]-1]:
            continue
        else:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    solution()