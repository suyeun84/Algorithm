import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
pref = []
result = 0

for _ in range(n):
    pre = list(map(int,input().strip().split()))
    pref.append(pre)

#치킨 3종류 택해서 만족도 가장 높게 만들기
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            res = 0
            for z in range(n):
                res += max(pref[z][i], pref[z][j], pref[z][k])
            result = max(result, res)
print(result)