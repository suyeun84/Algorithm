import sys
import heapq
import math


def solution():
    input = sys.stdin.readline
    N = int(input())
    word_sum = [0]*26
    answer = 0
    for _ in range(N):
        word = input().strip()
        l = len(word)
        for i in range(l):
            idx = ord(word[i]) - ord('A')
            word_sum[idx] += 10**(l-i-1)

    pq = []
    curr = 9
    for i in range(26):
        if word_sum[i] > 0:
            heapq.heappush(pq, (-word_sum[i]))

    while pq:
        sum = heapq.heappop(pq)
        answer += -sum*curr
        curr -= 1
    print(answer)


if __name__ == '__main__':
    solution()