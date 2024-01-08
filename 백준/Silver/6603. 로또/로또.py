import sys
input = sys.stdin.readline

def dfs(depth, curr, visited, num, result):
    if depth >= 6:
        print(' '.join(map(str, result)))
        return
    for i in range(curr+1, num[0]):
        if visited[i] == 0:
            visited[i] = 1
            result.append(num[i+1])
            dfs(depth+1, i, visited, num, result)
            visited[i] = 0
            result.pop()
    

while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break
    for i in range(num[0]-5):
        visited = [0]*num[0]
        result = []
        visited[i] = 1
        result.append(num[i+1])
        dfs(1, i, visited, num, result)

    print()