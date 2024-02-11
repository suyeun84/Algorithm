from collections import deque
def solution(arr):
    answer = []
    q = deque()
    q.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == q[-1]:
            continue
        else:
            q.append(arr[i])
    while q:
        answer.append(q.popleft())
    return answer