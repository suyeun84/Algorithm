import sys

def solution():
    input = sys.stdin.readline
    point = []
    for _ in range(3):
        point.append(list(map(int,input().split())))

    x1, y1 = point[0]
    x2, y2 = point[1]
    x3, y3 = point[2]
    val = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

    if val > 0:
        print(1)
    elif val < 0:
        print(-1)
    else:
        print(0)
        
        
if __name__ == '__main__':
    solution()
    