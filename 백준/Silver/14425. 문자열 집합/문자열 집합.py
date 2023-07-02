import sys
n, m = map(int, sys.stdin.readline().split())

S = []
result = 0
for _ in range(n):
    S.append(sys.stdin.readline())
for _ in range(m):
    result += S.count(sys.stdin.readline())
        
print(result)