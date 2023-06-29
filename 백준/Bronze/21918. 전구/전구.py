n, m = map(int, input().split())
current = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        current[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if current[i] == 0:
                current[i] = 1
            else:
                current[i] = 0
    elif a == 3:
        for i in range(b-1, c):
            current[i] = 0
    elif a == 4:
        for i in range(b-1, c):
            current[i] = 1
print(*current)