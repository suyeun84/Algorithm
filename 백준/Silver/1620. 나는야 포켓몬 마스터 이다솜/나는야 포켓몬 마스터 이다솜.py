import sys
n, m = map(int, input().split())

dict = {}
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    dict[i] = name
    dict[name] = i
for _ in range(m):
    got = sys.stdin.readline().strip()
    if got.isdigit():
        print(dict[int(got)])
    else:
        print(dict[got])