import sys
input = sys.stdin.readline
k, n = map(int, input().strip().split())
lans = [int(input().strip()) for _ in range(k)]
start, end = 1, max(lans)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt < n:
        end = mid - 1
    elif cnt >= n:
        start = mid + 1

print(end)