import sys

def solution():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    print(A/B)

if __name__ == '__main__':
    solution()