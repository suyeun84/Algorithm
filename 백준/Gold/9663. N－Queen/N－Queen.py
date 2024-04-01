import sys
input = sys.stdin.readline

N = int(input())
position = [0]*N
answer = 0

def backtracking(cnt):
    global answer
    if cnt == N:
        answer += 1
        return
    for i in range(N):
        position[cnt] = i
        flag = True
        for j in range(cnt):
            if position[cnt] == position[j] or abs(position[cnt]-position[j]) == abs(cnt-j):
                flag = False
                break
        if flag:
            backtracking(cnt+1)
    
backtracking(0)
print(answer)