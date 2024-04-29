import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    k = int(input())
    answer = 0
    start = 1
    end = k

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(1, N+1):
            if mid // i > N:
                cnt += N
            else:
                cnt += mid // i
        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    print(answer)


if __name__ == '__main__':
    solution()
