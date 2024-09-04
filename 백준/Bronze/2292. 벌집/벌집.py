def solution():
    N = int(input())
    if N == 1:
        print(1)
        return
    start = 2
    end = 7
    mid = 12
    answer = 2
    while N > end:
        start = start + mid
        end = end + mid
        mid += 6
        answer += 1
    print(answer)


if __name__ == '__main__':
    solution()
