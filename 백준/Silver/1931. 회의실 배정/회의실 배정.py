import sys

input = sys.stdin.readline
N = int(input())
meeting = []
for _ in range(N):
    a, b = map(int, input().strip().split())
    meeting.append([a,b])
meeting.sort(key=lambda x: (x[1], x[0]))

curr = 0
num = 0
for meet in meeting:
    start = meet[0]
    end = meet[1]
    if start >= curr:
        num += 1
        curr = end
print(num)