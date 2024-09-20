import sys

def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split(' '))
    S = input()
    check = [0]*N
    answer = 0

    for i in range(N):
        if S[i] == 'P':
            start, end = max(0, i - K), min(N, i + K + 1)
            for idx in range(start, end):
                if S[idx] == 'H' and check[idx] == 0:
                    check[idx] = 1
                    answer += 1
                    break

    print(answer)


if __name__ == '__main__':
    solution()