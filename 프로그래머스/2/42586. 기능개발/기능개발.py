from collections import deque
def solution(progresses, speeds):
    answer = []
    date = [0]*len(progresses)
    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            date[i] += 1
    day = date[0]
    cnt = 1
    for i in range(1, len(date)):
        if date[i] <= day:
            cnt += 1
            continue
        else:
            answer.append(cnt)
            cnt = 1
            day = date[i]
    answer.append(cnt)
    return answer