import sys

def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    answer = 0
    start = 0
    dict = {}
    for i in range(N):
        if num[i] in dict:
            dict[num[i]] += 1
            if dict[num[i]] > K:
                answer = max(answer, i - start)
                for j in range(start, i):
                    dict[num[j]] -= 1
                    if dict[num[j]] == K:
                        start = j + 1
                        break
        else:
            dict[num[i]] = 1
    answer = max(answer, N-start)
    print(answer)


if __name__ == '__main__':
    solution()
