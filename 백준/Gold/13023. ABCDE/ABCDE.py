import sys

def solution():
    answer = 0
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    if N < 5 or M < 4:
        return 0

    friend = [[] for _ in range(N)]
    visited = [0] * N

    for _ in range(M):
        a, b = map(int, input().split())
        friend[a].append(b)
        friend[b].append(a)

    def dfs(curr, v, depth):
        nonlocal answer
        if depth == 5:
            answer = 1
            return
        for f in friend[curr]:
            if v[f] == 0:
                v[f] = 1
                dfs(f, v, depth + 1)
                v[f] = 0
        return

    for i in range(N):
        visited[i] = 1
        dfs(i, visited, 1)
        visited[i] = 0
        if answer == 1:
            break
    print(answer)
    return


if __name__ == '__main__':
    solution()
