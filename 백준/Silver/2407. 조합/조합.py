n, m = map(int, input().split())

result = 1
if(n/2 < m):
    m = n - m
for i in range(m):
    result *= (n-i)
for i in range(m):
    result //= (m-i)
print(result)