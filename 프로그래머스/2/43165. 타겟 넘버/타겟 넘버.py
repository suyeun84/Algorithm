def solution(numbers, target):
    answer = 0
    def dfs(idx, cnt):
        nonlocal answer
        if cnt == target and idx == len(numbers)-1:
            answer += 1
            return
        if idx+1 >= len(numbers):
            return
        dfs(idx+1, cnt+numbers[idx+1])
        dfs(idx+1, cnt-numbers[idx+1])
        
    dfs(0, numbers[0])
    dfs(0, numbers[0]*(-1))
    return answer