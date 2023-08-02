tc = int(input())
for _ in range(tc):
    case = input()
    if case[0] == 'O':
        cnt = 1
        result = 1
    else:
        cnt = 0
        result = 0
    for i in range(1, len(case)):
        if case[i] == 'X':
            cnt = 0
            continue
        cnt += 1
        result += cnt
    print(result)