import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    building = list(map(int, input().split()))
    answer = 0

    for i in range(N):
        cnt = 0
        left_inc, right_inc = -1e9, -1e9
        #왼쪽
        for j in range(i-1, -1, -1):
            inc = (building[i] - building[j]) / (j - i)
            if inc > left_inc:
                cnt += 1
                left_inc = inc
        #오른쪽
        for j in range(i+1, N):
            inc = (building[i] - building[j]) / (i - j)
            if inc > right_inc:
                cnt += 1
                right_inc = inc
        answer = max(answer, cnt)
    print(answer)


if __name__ == '__main__':
    solution()
