import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    x = list(map(int, input().strip().split(' ')))
    dist = x[0] * 2
    for i in range(M):
        if i == M-1:
            dist = max(dist, (N-x[i])*2)
        else:
            dist = max(dist, x[i+1]-x[i])
    if dist % 2 == 0:
        print(dist//2)
    else:
        print(dist//2+1)


if __name__ == '__main__':
    solution()