import sys


def solution():
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    
    def multi(a, n):
        if n == 1:
            return a % C
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * a) % C
    
    print(multi(A, B))


if __name__ == '__main__':
    solution()
