from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    if cacheSize == 0:
        return 5*len(cities)
    for city in cities:
        low_city = city.lower()
        if len(q) == 0:
            q.append(low_city)
            answer += 5
            continue
        if low_city in q:
            q.remove(low_city)
            q.append(low_city)
            answer += 1
        else:
            if len(q) == cacheSize:
                q.popleft()
            q.append(low_city)
            answer += 5
    return answer