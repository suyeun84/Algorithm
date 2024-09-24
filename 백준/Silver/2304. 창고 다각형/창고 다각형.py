import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    arr = []
    answer = 0
    for _ in range(N):
        L, H = map(int, input().split())
        arr.append([L,H]) #[위치, 높이]

    arr.sort(key=lambda x: -x[1])

    mid = arr[0][0]
    answer += arr[0][1]
    left = mid
    right = mid+1
    for i in range(1, N):
        if arr[i][0] < left:
            answer += (left-arr[i][0])*arr[i][1]
            left = arr[i][0]
        elif arr[i][0]+1 > right:
            answer += (arr[i][0]+1-right) * arr[i][1]
            right = arr[i][0]+1

    print(answer)


if __name__ == '__main__':
    solution()
