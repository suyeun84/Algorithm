import sys

def solution():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        curr = 0
        answer = 0
        check = [0] * N
        price = list(map(int, input().split(' ')))
        sorted_price = []
        for i in range(N):
            sorted_price.append([price[i], i])
        sorted_price = sorted(sorted_price, key=lambda x:-x[0])

        for i in range(N):
            p = sorted_price[i][0]
            idx = sorted_price[i][1]
            if idx > curr:
                for j in range(curr, idx):
                    if check[j] == 0:
                        answer += (p-price[j])
                        check[j] = 1
                curr = idx
            check[idx] = 1
            if curr == N-1:
                break
        print(answer)


if __name__ == '__main__':
    solution()
