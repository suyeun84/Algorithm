import sys


def solution():
    input = sys.stdin.readline
    num = list(input().strip())
    n = 0
    idx = 0
    while True:
        n += 1
        for s in str(n):
            if s == num[idx]:
                idx += 1
                if idx == len(num):
                    print(n)
                    return


if __name__ == '__main__':
    solution()
