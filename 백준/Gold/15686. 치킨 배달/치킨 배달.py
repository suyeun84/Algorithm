import sys
from collections import deque
from itertools import combinations

def solution() :
    input = sys.stdin.readline
    board = []
    answer = int(1e9)
    N, M = map(int, input().split())

    for _ in range(N):
        board.append(list(map(int, input().split())))

    def calculate(M_chicken):
        total = 0
        dist = [int(1e9)]*len(house)
        for ci, cj in M_chicken:
            for i in range(len(house)):
                l = abs(ci-house[i][0]) + abs(cj-house[i][1])
                if dist[i] > l:
                    dist[i] = l
        for d in dist:
            total += d
        return total

    chicken = []
    house = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                chicken.append([i, j])
            elif board[i][j] == 1:
                house.append([i, j])

    for M_chicken in combinations(chicken, M):
        result = calculate(M_chicken)
        if result < answer:
            answer = result
    print(answer)


if __name__ == '__main__':
    solution()
