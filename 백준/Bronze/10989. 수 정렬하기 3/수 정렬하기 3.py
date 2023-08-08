import sys
input = sys.stdin.readline

cnt = [0] * 10001
n = int(input())
for _ in range(n):
    cnt[int(input())] += 1
for i in range(10001):
    for _ in range(cnt[i]):
        print(i)