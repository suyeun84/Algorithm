import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    connect = list(map(int, input().split()))
    answer = []

    def check(index):
        start = 0
        end = len(answer) - 1
        while start < end:
            mid = (start + end) // 2
            if answer[mid] > connect[index]:
                end = mid
            elif answer[mid] < connect[index]:
                start = mid+1
        return end

    for i in range(N):
        if i == 0:
            answer.append(connect[i])
        else:
            if answer[-1] < connect[i]:
                answer.append(connect[i])
            else:
                answer[check(i)] = connect[i]

    print(len(connect)-len(answer))


if __name__ == '__main__':
    solution()
