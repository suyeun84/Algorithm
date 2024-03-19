from itertools import product
def solution(word):
    answer = 0
    alpa = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(it):
        nonlocal answer
        if it == word:
            return True
        if len(it) >= 5:
            return False
        for a in alpa:
            answer += 1
            if(dfs(it+a)):
                return True
            
    #dfs('')
    words = []
    for i in range(1,6):
        for s in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            words.append(s)
    words.sort()
    answer = words.index(word)
    
    return answer