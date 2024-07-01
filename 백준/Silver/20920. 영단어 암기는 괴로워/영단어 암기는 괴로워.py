import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    words = {}
    for _ in range(N):
        word = input().strip()
        if len(word) < M:
            continue
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for word in sorted_words:
        print(word[0])


if __name__ == '__main__':
    solution()
