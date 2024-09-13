import sys


def solution():
    input = sys.stdin.readline
    s = input().strip()
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(3):
                stack.pop()
    if len(stack) == 1 and stack[0] == 'P':
        print('PPAP')
    else:
        print('NP')


if __name__ == '__main__':
    solution()
