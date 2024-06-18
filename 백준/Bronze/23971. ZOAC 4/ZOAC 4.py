import sys
import math


def solution():
    input = sys.stdin.readline
    H, W, N, M = map(int, input().split())

    a = math.ceil(H/(N+1))
    b = math.ceil(W/(M+1))
    print(a*b)


if __name__ == '__main__':
    solution()