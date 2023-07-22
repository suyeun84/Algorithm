import sys
input = sys.stdin.readline

result = 0
n = int(input())
dic = {}
for i in range(n):
    cmd = input().strip()
    if cmd == "ENTER":
        dic = {}
        continue
    if cmd not in dic:
        dic[cmd] = 1
        result += 1
print(result)