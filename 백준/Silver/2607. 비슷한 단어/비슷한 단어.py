import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    arr = [0]*26
    target = list(input().strip())
    answer = 0
    for s in target:
        arr[ord(s)-65] += 1
    for i in range(N-1):
        alpa = [0]*26
        cnt = 0
        word = list(input().strip())
        for s in word:
            alpa[ord(s)-65] += 1
        for j in range(26):
            cnt += abs(arr[j]-alpa[j])
        if cnt <= 1 or (len(word) == len(target) and cnt == 2):
            answer += 1
    print(answer)


if __name__ == '__main__':
    solution()
