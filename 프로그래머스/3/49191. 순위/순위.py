#플로이드-워셜 알고리즘
def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for result in results:
        win = result[0] - 1
        lose = result[1] - 1
        graph[win][lose] = 1
        graph[lose][win] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] == 0:
                cnt += 1
        if cnt == 1:
            answer += 1
    return answer