testcase = int(input())

for _ in range(testcase):
    cnt = int(input())
    num = map(int, input().split())
    max = -1000000
    min = 1000000
    for i in num:
        if(max < i):
            max = i
        if(min > i):
            min = i
    print(min, max)