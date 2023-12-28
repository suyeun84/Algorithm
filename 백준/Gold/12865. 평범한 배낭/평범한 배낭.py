import sys

input = sys.stdin.readline
products = []

N, K = map(int, input().split())
for _ in range(N):
    w, v = map(int, input().split())
    products.append((w, v))
    
dp = [0]*(K+1)
for product in products:
    w, v = product
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)
print(dp[-1])