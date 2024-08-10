import sys
import heapq


def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    jew = []
    bag = []
    answer = 0
    for _ in range(N):
        M, V = map(int, input().split())
        jew.append([M, V])
    jew.sort(key=lambda x: x[0], reverse=True)
    for _ in range(K):
        bag.append(int(input()))
    bag.sort(reverse=True)
    hq = []

    while bag:
        bag_size = bag.pop()
        while jew:
            weight, val = jew.pop()
            if weight <= bag_size:
                heapq.heappush(hq, -val)
            else:
                jew.append([weight, val])
                break
        if hq:
            answer -= heapq.heappop(hq)

    print(answer)


if __name__ == '__main__':
    solution()
