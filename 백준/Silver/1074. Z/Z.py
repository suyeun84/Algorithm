import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
result = 0

while True:
    if(N == 1):
        print(result+2*r+c)
        break

    if r < 2**(N-1) and c >= 2**(N-1):
        #1사분면
        c -= 2**(N-1)
        result += (2**(N-1))*(2**(N-1))
    elif r >= 2**(N-1) and c < 2**(N-1):
        #3사분면
        r -= 2**(N-1)
        result += (2**(N-1))*(2**(N-1))*2
    elif r >= 2**(N-1) and c >= 2**(N-1):
        #4사분면
        r -= 2**(N-1)
        c -= 2**(N-1)
        result += (2**(N-1))*(2**(N-1))*3
    N -= 1