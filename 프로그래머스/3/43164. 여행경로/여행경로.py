def solution(tickets):
    answer = []
    visited = [0]*len(tickets)
    
    def dfs(curr, res):
        if len(res) == len(tickets)+1:
            answer.append(res)
            return
        for idx in range(len(tickets)):
            if tickets[idx][0] == curr and visited[idx] == 0:
                visited[idx] = 1
                dfs(tickets[idx][1], res + [tickets[idx][1]])
                visited[idx] = 0
            
            
    dfs('ICN', ['ICN'])
    answer.sort()
    return answer[0]