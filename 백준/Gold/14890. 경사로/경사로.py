import sys

def solution():
    input = sys.stdin.readline
    N, L = map(int, input().split())
    board = []
    answer = 0
    for _ in range(N):
        board.append(list(map(int, input().split())))

    def checkRow(row):
        #row 고정
        col = 1
        cnt = 1
        while col < N:
            if abs(board[row][col-1] - board[row][col]) > 1:
                return False
            if board[row][col-1] == board[row][col]:
                cnt += 1
                col += 1
            elif board[row][col-1] > board[row][col]:
                #이전꺼가 높음
                cnt = 1
                num = board[row][col]
                for i in range(1, L-cnt+1):
                    if col + i >= N:
                        return False
                    if board[row][col + i] != num:
                        return False
                col += L-cnt+1
                cnt = 0

            elif board[row][col-1] < board[row][col]:
                # 이후꺼가 높음
                if cnt >= L:
                    col += 1
                    cnt = 1
                    continue
                else:
                    return False
        return True

    def checkCol(col):
        #col 고정
        row = 1
        cnt = 1
        while row < N:
            if abs(board[row-1][col] - board[row][col]) > 1:
                return False
            if board[row-1][col] == board[row][col]:
                cnt += 1
                row += 1
            elif board[row-1][col] > board[row][col]:
                #이전꺼가 높음
                cnt = 1
                num = board[row][col]
                for i in range(1, L-cnt+1):
                    if row + i >= N:
                        return False
                    if board[row + i][col] != num:
                        return False
                row += L-cnt+1
                cnt = 0

            elif board[row-1][col] < board[row][col]:
                # 이후꺼가 높음
                if cnt >= L:
                    row += 1
                    cnt = 1
                    continue
                else:
                    return False
        return True
  
    # 가로
    for i in range(N):
        if checkRow(i):
            answer += 1
    # 세로
        if checkCol(i):
            answer += 1
    print(answer)

if __name__ == '__main__':
    solution()