import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    port = list(map(int, input().split()))
    answer = []

    def find(s,e,t):
        while s < e:
            m = (s+e) // 2
            if answer[m] <= t:
                s = m + 1
            else:
                e = m
        return e

    for i in range(n):
        if i == 0:
            answer.append(port[0])
            continue
        if port[i] > answer[-1]:
            answer.append(port[i])
        else:
            answer[find(0, len(answer), port[i])] = port[i]
    print(len(answer))


if __name__ == '__main__':
    solution()
    