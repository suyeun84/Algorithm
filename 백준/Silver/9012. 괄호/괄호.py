import sys
n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    stack = []
    for i in line:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')