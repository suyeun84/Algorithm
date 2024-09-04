def solution():
    N = int(input())
    if N == 1:
        print(1)
        return
    num = 1
    for i in range(N):
        num += 6*i
        if N <= num:
            print(i+1)
            break

if __name__ == '__main__':
    solution()
