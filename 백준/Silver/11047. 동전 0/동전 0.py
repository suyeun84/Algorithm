import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())

coin = []
cnt = 0

for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

for money in coin:
    cnt += K // money
    K %= money
print(cnt)