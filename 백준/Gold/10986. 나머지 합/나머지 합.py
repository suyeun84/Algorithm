import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    res = [0]*M
    sum = 0

    for i in num:
        sum += i
        res[sum % M] += 1
    
    answer = res[0]
    for i in range(M):
        answer += res[i] * (res[i]-1) // 2

    print(answer)


if __name__ == '__main__':
    solution()
