def dfs(curr, target, words, visited, num, answer):
    #curr words 중 visited가 False인 애들 중에 다른 알파벳 1개인거 찾기
    #만약 target과 같으면 return
    #print("in dfs="+curr)
    #print(num)
    if words[words.index(curr)] == target:
        answer.append(num)
        return
    
    for index in range(len(words)):
        if visited[index] == True:
            continue
        diff = 0
        word = words[index]
        #print("word="+word)
        for i in range(len(curr)):
            if curr[i] != word[i]:
                diff += 1
        if diff == 1:
            visited[words.index(curr)] = True
            dfs(word, target, words, visited, num+1, answer)
            visited[words.index(curr)] = False
            

def solution(begin, target, words):
    answer = []
    visited = [False for _ in range(len(words))]
    if target not in words:
        return 0
    
    for word in words:
        diff = 0
        for i in range(len(begin)):
            if begin[i] != word[i]:
                diff += 1
        if diff == 1:
            dfs(word, target, words, visited, 1, answer)
        
    return min(answer)