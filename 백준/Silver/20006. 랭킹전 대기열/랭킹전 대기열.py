import sys

def solution():
    input = sys.stdin.readline
    p, m = map(int, input().split(' '))
    room = []
    for _ in range(p):
        l, n = map(str, input().strip().split(' '))
        flag = True
        for i in range(len(room)):
            if len(room[i]) < m and abs(int(room[i][0][0]) - int(l)) <= 10:
                room[i].append([l, n])
                flag = False
                break
        if flag:
            room.append([[l, n]])

    for i in range(len(room)):
        room[i].sort(key=lambda x: x[1])
        if len(room[i]) == m:
            print("Started!")
        else:
            print("Waiting!")
        for j in range(len(room[i])):
            print(room[i][j][0]+' '+room[i][j][1])


if __name__ == '__main__':
    solution()
