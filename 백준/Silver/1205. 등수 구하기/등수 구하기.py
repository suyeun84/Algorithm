import sys


def solution():
    input = sys.stdin.readline
    N, S, P = map(int, input().split())
    if N == 0:
        print(1)
        return
    score = list(map(int, input().split()))
    score.sort(reverse= True)
    if len(score) == P:
        if score[-1] >= S:
            print(-1)
            return
    for i in range(len(score)):
        if score[i] <= S:
            print(i+1)
            return
    print(len(score)+1)


if __name__ == '__main__':
    solution()
