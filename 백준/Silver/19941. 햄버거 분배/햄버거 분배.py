import sys

def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split(' '))
    S = input()
    check = [0]*N
    answer = 0

    for i in range(N):
        if S[i] == 'P':
            start = i-K
            end = i+K+1
            if i-K < 0:
                start = 0
            if i+K+1 > N:
                end = N
            for idx in range(start, end):
                if S[idx] == 'H' and check[idx] == 0:
                    check[idx] = 1
                    answer += 1
                    break

    print(answer)


if __name__ == '__main__':
    solution()