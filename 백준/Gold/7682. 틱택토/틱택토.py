import sys

def solution():
    input = sys.stdin.readline

    def find_bingo(str):
        # 가로
        for i in range(0, 9, 3):
            if board[i] == str and board[i] == board[i + 1] == board[i + 2]:
                return True
        # 세로
        for i in range(3):
            if str == board[i] and board[i] == board[i + 3] == board[i + 6]:
                return True
        # 대각선
        if str == board[0] and board[0] == board[4] == board[8]:
            return True
        if str == board[2] and board[2] == board[4] == board[6]:
            return True
        return False

    while True:
        board = input().strip()
        if board == 'end':
            break
        O_cnt, X_cnt = board.count('O'), board.count('X')
        O_bingo, X_bingo = find_bingo('O'), find_bingo('X')
        if X_bingo and not O_bingo and X_cnt == O_cnt + 1:
            print('valid')
            continue
        if O_bingo and not X_bingo and O_cnt == X_cnt:
            print('valid')
            continue
        if not O_bingo and not X_bingo and O_cnt + X_cnt == 9 and X_cnt > O_cnt:
            print('valid')
            continue
        print('invalid')


if __name__ == '__main__':
    solution()
