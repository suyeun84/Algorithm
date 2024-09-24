import sys

def solution():
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        price = list(map(int, input().split()))
        money = 0
        maxPrice = 0
        for i in range(len(price)-1, -1, -1):
            if price[i] > maxPrice:
                maxPrice = price[i]
            else:
                money += maxPrice - price[i]
        print(money)


if __name__ == '__main__':
    solution()
