N, M = map(int, input().split())
answer = []

def backtracking(x):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(x, N+1):
        if i not in answer:
            answer.append(i)
            backtracking(i+1)
            answer.pop()
    
backtracking(1)