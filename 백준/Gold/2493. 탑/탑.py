import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    tower = list(map(int, input().split()))
    answer = [0]*N
    stack = []
    stack.append([tower[0], 1])


    for i in range(1, N):
        while stack:
            if tower[i] > stack[-1][0]:
                stack.pop()
            else:
                answer[i] = stack[-1][1]
                break

        stack.append([tower[i],i+1])
    print(*answer)

if __name__ == '__main__':
    solution()
