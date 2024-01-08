import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, plus, minus, multi, div, result):
    global maximum
    global minimum
    if depth == N:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return
    if plus > 0:
        dfs(depth+1, plus-1, minus, multi, div, result+A[depth])
    if minus > 0:
        dfs(depth+1, plus, minus-1, multi, div, result-A[depth])
    if multi > 0:
        dfs(depth+1, plus, minus, multi-1, div, result*A[depth])
    if div > 0:
        dfs(depth+1, plus, minus, multi, div-1, int(result/A[depth]))
    

dfs(1, op[0], op[1], op[2], op[3], A[0])
print(maximum)
print(minimum)