def solution(dirs):
    answer = 0
    x, y = 0, 0
    visited = set()
    for dir in dirs:
        if dir == "U" and y+1 <= 5:
            visited.add((x,y, x,y+1))
            visited.add((x,y+1, x,y))
            y += 1
        elif dir == "D" and y-1 >= -5:
            visited.add((x,y, x,y-1))
            visited.add((x,y-1, x,y))
            y -= 1
        elif dir == "R" and x+1 <= 5:
            visited.add((x,y, x+1,y))
            visited.add((x+1,y, x,y))
            x += 1
        elif dir == "L" and x-1 >= -5:
            visited.add((x,y, x-1,y))
            visited.add((x-1,y, x,y))
            x -= 1
        else:
            continue
    answer = len(visited)//2
    return answer