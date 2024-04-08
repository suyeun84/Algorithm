import sys


def solution():
    input = sys.stdin.readline
    n, c = map(int, input().split())
    x = []
    for _ in range(n):
        x.append(int(input()))
    x.sort()

    start, end = 0, x[n-1]-x[0]
    while start <= end: #최대 거리
        cnt = 1
        curr = x[0]
        #x[0]에서 시작해서 cnt개만큼 위치시킬 수 있는지
        mid = (start+end)//2
        for i in range(1, n):
            if curr + mid <= x[i]:
                curr = x[i]
                cnt += 1

        if cnt >= c:
            start = mid + 1
        elif cnt < c:
            end = mid - 1
    print(end)


if __name__ == '__main__':
    solution()
