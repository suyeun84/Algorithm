import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    people = []
    for i in range(N):
        w, h = map(int, input().split(' '))
        people.append([w, h])
    answer = [1]*N
    for i in range(N):
        cnt = 1
        for j in range(N):
            if i == j:
                continue
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                cnt += 1
        answer[i] = cnt
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    solution()
