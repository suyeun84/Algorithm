N = int(input())

for i in range(N):
    str = ''
    for _ in range(N-i-1):
        str += ' '
    for _ in range(i+1):
        str += '*'
    print(str)