import sys

def solution():
    input = sys.stdin.readline
    left = list(input().strip())
    right = []
    M = int(input())
    for _ in range(M):
        word = list(input().strip().split(' '))
        if word[0] == 'L' and left:
            right.append(left.pop())
        elif word[0] == 'D' and right:
            left.append(right.pop())
        elif word[0] == 'B' and left:
            left.pop()
        elif word[0] == 'P':
            left.append(word[1])

    answer = left + right[::-1]
    print(''.join(answer))


if __name__ == '__main__':
    solution()
