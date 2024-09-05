import sys

def solution():
    input = sys.stdin.readline

    M = int(input())
    answer = set()
    for _ in range(M):
        line = input().strip().split(' ')
        if line[0] == "all" or line[0] == "empty":
            op = line[0]
        else:
            op, x = line[0], int(line[1])
        if op == 'add':
            answer.add(x)
        elif op == 'remove' and len(answer) > 0:
            answer.remove(x)
        elif op == 'check':
            if len(answer) > 0 and x in answer:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if len(answer) > 0 and x in answer:
                answer.remove(x)
            else:
                answer.add(x)
        elif op == 'all':
            answer.clear()
            answer.update(i for i in range(1, 21))
        elif op == 'empty':
            answer.clear()


if __name__ == '__main__':
    solution()
