import sys


def solution():
    input = sys.stdin.readline
    N, M, L, K = map(int, input().split())
    position = []
    answer = K
    for _ in range(K):
        y, x = map(int, input().split())
        position.append([y, x])

    for s1 in position: # y범위
        for s2 in position: # x범위
            cnt = 0
            for s3 in position:
                if s1[0] <= s3[0] <= s1[0]+L and s2[1] <= s3[1] <= s2[1]+L:
                    cnt += 1
            answer = min(answer, K-cnt)

    print(answer)


if __name__ == '__main__':
    solution()
