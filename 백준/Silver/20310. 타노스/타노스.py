import sys

def solution():
    input = sys.stdin.readline
    S = input().strip()
    cnt = [0]*2
    answer = ''
    for s in S:
        if s == '1':
            cnt[1] += 1
        else:
            cnt[0] += 1
    cnt[0], cnt[1] = cnt[0]//2, cnt[1]//2
    for s in S:
        if s == '1' and cnt[1] > 0:
            cnt[1] -= 1
            continue
        if s == '0':
            if cnt[0] > 0:
                cnt[0] -= 1
                answer += s
            continue
        answer += s
    print(answer)


if __name__ == '__main__':
    solution()
