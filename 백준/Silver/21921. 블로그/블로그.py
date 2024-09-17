import sys

def solution():
    input = sys.stdin.readline
    N, X = map(int, input().split())
    visit = list(map(int, input().strip().split(' ')))
    current_sum = sum(visit[:X])
    max_visit = current_sum
    cnt = 1
    for i in range(X, N):
        current_sum += visit[i] - visit[i-X]
        if max_visit < current_sum:
            cnt = 1
            max_visit = current_sum
        elif max_visit == current_sum:
            cnt += 1
    if max_visit == 0:
        print('SAD')
    else:
        print(max_visit)
        print(cnt)


if __name__ == '__main__':
    solution()
