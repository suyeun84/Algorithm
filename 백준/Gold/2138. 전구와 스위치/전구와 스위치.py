import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    curr_state = list(map(int, input().strip()))
    target_state = list(map(int, input().strip()))

    def change(cnt, curr_state):
        curr_copy = curr_state[:]
        for i in range(1, N):
            if curr_copy[i-1] == target_state[i-1]:
                continue
            cnt += 1
            for j in range(i-1, i+2):
                if j < N:
                    curr_copy[j] = 1 - curr_copy[j]
        if curr_copy == target_state:
            return cnt
        else:
            return 1e9

    # 첫번째꺼 안누름
    answer = change(0, curr_state)
    # 첫번째꺼 누름
    curr_state[0] = 1 - curr_state[0]
    curr_state[1] = 1 - curr_state[1]
    answer = min(answer, change(1, curr_state))
    if answer != 1e9:
        print(answer)
    else:
        print(-1)


if __name__ == '__main__':
    solution()
