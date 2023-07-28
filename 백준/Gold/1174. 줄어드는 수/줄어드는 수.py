import sys
input = sys.stdin.readline

n = int(input())
result = set()
num = []

def dfs():
    if num:
        result.add(int(''.join(map(str, num))))
    for i in range(10):
        if not num or num[-1] > i:
            num.append(i)
            dfs()
            num.pop()
    
dfs()
result = sorted(result)
print(result[n-1] if len(result) >= n else -1)