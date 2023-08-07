import sys
input = sys.stdin.readline
n = int(input())
score = list(map(int, input().strip().split()))
sum = 0
max_score = max(score)
for i in range(n):
    sum += (score[i] / max_score * 100)
print(sum/n)