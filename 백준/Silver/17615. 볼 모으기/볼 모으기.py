import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    balls = input().strip()
    red, blue = 0, 0
    for i in range(N):
        if balls[i] == 'R':
            red += 1
        else:
            blue += 1
    answer = min(red, blue)

    cnt = 1
    for i in range(1, N):
        if balls[i] == balls[i-1]:
            cnt += 1
        else:
            break
    if balls[0] == 'R':
        answer = min(answer, red-cnt)
    else:
        answer = min(answer, blue-cnt)

    cnt = 1
    for i in range(N-2, -1, -1):
        if balls[i] == balls[i + 1]:
            cnt += 1
        else:
            break
    if balls[N-1] == 'R':
        answer = min(answer, red - cnt)
    else:
        answer = min(answer, blue - cnt)

    print(answer)


if __name__ == '__main__':
    solution()
