import sys
input = sys.stdin.readline
n = int(input())
total = []
result = 1 << 100

def brute(pre, sour, bitter):
    global result
    sour *= total[pre][0]
    bitter += total[pre][1]
    result = min(result, abs(sour-bitter))
    for j in range(pre+1, n):
        brute(j, sour, bitter)

for _ in range(n):
    total.append(list(map(int, input().split())))

for i in range(0,n):
    brute(i, 1, 0)
    
print(result)