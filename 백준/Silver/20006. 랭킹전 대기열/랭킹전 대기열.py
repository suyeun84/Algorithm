import sys

def solution():
    input = sys.stdin.readline
    p, m = map(int, input().split(' '))
    room = []
    for _ in range(p):
        l, n = map(str, input().strip().split(' '))
        flag = False
        if len(room) == 0:
            room.append([[l, n]])
            continue
        for i in range(len(room)):
            if len(room[i]) == m:
                flag = True
                continue
            if abs(int(room[i][0][0]) - int(l)) <= 10:
                room[i].append([l, n])
                flag = False
                break
            else:
                flag = True
        if flag:
            room.append([[l, n]])

    for i in range(len(room)):
        room[i].sort(key=lambda x: x[1])
        if len(room[i]) == m:
            print("Started!")
            for j in range(m):
                print(room[i][j][0]+' '+room[i][j][1])
        else:
            print("Waiting!")
            for j in range(len(room[i])):
                print(room[i][j][0]+' '+room[i][j][1])


if __name__ == '__main__':
    solution()
