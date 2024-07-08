import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    word_sum = {}
    curr = 9
    answer = 0
    for _ in range(N):
        word = input().strip()
        l = len(word)
        for i in range(l):
            if word[i] in word_sum:
                word_sum[word[i]] += 10**(l-i-1)
            else:
                word_sum[word[i]] = 10**(l-i-1)

    lst = sorted(word_sum.items(), key=lambda x: x[1], reverse=True)
    for l in lst:
        answer += curr * l[1]
        curr -= 1
    print(answer)


if __name__ == '__main__':
    solution()