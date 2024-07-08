import heapq
def solution(picks, minerals):
    answer = 0
    pq = []
    cnt = 0
    dia, iron, stone = 0,0,0
    for mine in minerals:
        if cnt == 5:
            cnt = 0
            heapq.heappush(pq, (-1*stone, -1*iron, -1*dia))
            dia, iron, stone = 0,0,0
        if mine == "diamond":
            dia += 1
            iron += 5
            stone += 25
        elif mine == "iron":
            dia += 1
            iron += 1
            stone += 5
        elif mine == "stone":
            dia += 1
            iron += 1
            stone += 1
        cnt += 1
    if len(minerals) / 5 <= picks[0] + picks[1] + picks[2]:
        if dia != 0 or iron != 0 or stone != 0:
            heapq.heappush(pq, (-1*stone, -1*iron, -1*dia))
    
    while pq:
        print(pq)
        print(answer)
        if picks[0] == 0 and picks[1] == 0 and picks[2] == 0:
            break
        if picks[0] > 0:
            answer += -1*heapq.heappop(pq)[2]
            picks[0] -= 1
            continue
        elif picks[1] > 0:
            answer += -1*heapq.heappop(pq)[1]
            picks[1] -= 1
            continue
        elif picks[2] > 0:
            answer += -1*heapq.heappop(pq)[0]
            picks[2] -= 1
            continue
    return answer