import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    dic = {}
    for _ in range(N):
        dic[input().strip()] = 1
    for _ in range(M):
        words = list(map(str, input().strip().split(',')))
        cnt = 0
        for word in words:
            if word in dic:
                del dic[word]
        print(len(dic))


if __name__ == '__main__':
    solution()
