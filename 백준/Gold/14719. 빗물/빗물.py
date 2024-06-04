import sys


def solution():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    block = list(map(int, input().split(" ")))
    answer = 0

    for i in range(1, len(block)-1):
        left = max(block[0:i])
        right = max(block[i:len(block)])
        m = min(left, right)
        if m - block[i] > 0:
            answer += (m - block[i])

    print(answer)


if __name__ == '__main__':
    solution()