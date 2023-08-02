import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))
result = sorted(result)
for i in result:
    print(i)