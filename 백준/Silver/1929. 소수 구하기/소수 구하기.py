M, N = map(int, input().split())
for num in range(M, N+1):
    if num == 1:
        continue
    flag = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            flag = False
            break
    if(flag):
        print(num)