from collections import deque
def dfs(n, computers, idx, visited):
    for i in range(n):
        if computers[idx][i] == 1 and idx != i and visited[i] == False:
            visited[i] = True
            dfs(n, computers, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(n, computers, i, visited)
            answer += 1
    return answer