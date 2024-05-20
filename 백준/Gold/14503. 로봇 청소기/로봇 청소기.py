import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    R, C, D = map(int, input().split())
    # 북=0, 동=1, 남=2, 서=3
    board = []
    dir = [[-1,0], [0,1], [1,0], [0,-1]]
    for i in range(N):
        board.append(list(map(int, input().split())))
    # 청소되지 않음=0, 벽=1

    def dfs(r,c,d):
        cnt = 0
        while True:
            # 현재 칸 청소되지 않았으면 청소
            if board[r][c] == 0:
                board[r][c] = 2
                cnt += 1
            # 주변 4칸 중 청소되지 않은 빈 칸 있으면 -> 반시계 방향 90도 회전 -> 전진
            for _ in range(4):
                d -= 1
                if d < 0:
                    d = 3
                if board[r + dir[d][0]][c + dir[d][1]] == 0:
                    r = r + dir[d][0]
                    c = c + dir[d][1]
                    break

            # 주변 4칸 중 청소되지 않은 빈 칸 없으면
            # 바라보는 방향 유지한 채 한 칸 후진
            # 바라보는 방향의 뒤쪽이 벽이면 작동 멈춤
            else:
                r = r + dir[d][0]*-1
                c = c + dir[d][1]*-1
                if board[r][c] == 1:
                    print(cnt)
                    return


    dfs(R,C,D)


if __name__ == '__main__':
    solution()
