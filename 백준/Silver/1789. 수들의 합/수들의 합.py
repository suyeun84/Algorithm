s = int(input())
cnt = 1
while(s >= cnt):
    s -= cnt
    cnt += 1
print(cnt-1)