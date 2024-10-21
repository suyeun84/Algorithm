import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    building = []
    answer = 0
    for _ in range(n):
        x, y = map(int, input().split())
        building.append([y, x])
    stack = []
    for i in range(n):
        while stack and stack[-1] > building[i][0]:
            stack.pop()
        if not stack or stack[-1] < building[i][0]:
            if building[i][0] == 0:
                continue
            stack.append(building[i][0])
            answer += 1
    print(answer)


if __name__ == '__main__':
    solution()
