import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    num = list(map(int, input().strip().split()))
    total = 0
    for i in range(1, num[0]+1):
        for j in range(i+1, num[0]+1):
            start = min(num[i], num[j])
            for k in range(start, 0, -1):
                if num[i] % k == 0 and num[j] % k == 0:
                    total += k
                    break
    print(total)