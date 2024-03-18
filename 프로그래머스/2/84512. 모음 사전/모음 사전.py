def solution(word):
    answer = 0
    alpa = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(it):
        nonlocal answer
        if it == word:
            return True
        if len(it) == 5:
            return False
        for a in alpa:
            answer += 1
            if len(it+a) > 5:
                return False
            if(dfs(it+a)):
                return True
            
    dfs('')
    return answer