import sys


def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    lecture = list(map(int, input().split()))

    start = max(lecture)
    end = 0
    for i in range(N):
        end += lecture[i]

    while start <= end:
        mid = int((start + end) / 2)
        sum = 0
        cnt = 0
        for i in range(N):
            if sum + lecture[i] > mid:
                cnt += 1
                sum = 0
            sum += lecture[i]
        if sum != 0:
            cnt += 1
        if cnt > M:
            start = mid + 1
        else:
            end = mid - 1

    print(start)


if __name__ == '__main__':
    solution()
