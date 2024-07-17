import sys


def solution():
    input = sys.stdin.readline
    board = []
    zero = []
    for _ in range(9):
        board.append(list(map(int, input().split())))

    def search_row(target, y):
        for i in range(9):
            if board[y][i] == target:
                return True
        return False

    def search_column(target, x):
        for i in range(9):
            if board[i][x] == target:
                return True
        return False

    def search_square(target, y, x):
        ny = (y//3)*3
        nx = (x//3)*3
        for i in range(3):
            for j in range(3):
                if board[ny+i][nx+j] == target:
                    return True
        return False

    def search(idx):
        if idx == len(zero):
            for i in range(9):
                print(*board[i])
            exit()
        y = zero[idx][0]
        x = zero[idx][1]

        for num in range(1, 10):
            if search_row(num, y) or search_column(num, x) or search_square(num, y, x):
                continue
            board[y][x] = num
            search(idx + 1)
            board[y][x] = 0

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zero.append([i,j])
    search(0)


if __name__ == '__main__':
    solution()
