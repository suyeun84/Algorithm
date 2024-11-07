import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    words = [input().strip() for _ in range(N)]
    dic = {}

    for word in words:
        tmp = ''
        for ch in word:
            tmp += ch
            dic[tmp] = dic.get(tmp, 0) + 1

    answer, max_len = '', 0
    for word, cnt in dic.items():
        word_len = len(word)
        if cnt > 1 and word_len > max_len:
            answer = word
            max_len = word_len

    cnt = 0
    for word in words:
        if answer == word[:max_len]:
            cnt += 1
            print(word)
        if cnt == 2:
            break


if __name__ == '__main__':
    solution()
