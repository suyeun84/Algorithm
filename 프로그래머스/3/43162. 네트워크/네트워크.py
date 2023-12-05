def dfs(n, visited, computers, com):
    visited[com] = True
    for link in range(n):
        if link != com and computers[com][link] == 1 and visited[link] == False:
            dfs(n, visited, computers, link)
    

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, visited, computers, com)
            answer += 1
    return answer