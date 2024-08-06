import sys

def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    T = int(input())

    def dfs(target, answer):
        visited[target] = 1
        cycle.append(target)
        curr = num[target]

        if visited[curr]:
            if curr in cycle:
                answer += cycle[cycle.index(curr):]
            return
        else:
            dfs(curr, answer)

    for _ in range(T):
        n = int(input())
        num = [0] + list(map(int, input().split()))
        answer = []
        visited = [0]*(n+1)
        
        for i in range(1, n+1):
            if not visited[i]:
                cycle = []
                dfs(i, answer)

        print(n-len(answer))


if __name__ == '__main__':
    solution()