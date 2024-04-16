import math
def solution(n,a,b):
    answer = 1

    k = 2
    while True:
        if math.ceil(a/k) == math.ceil(b/k):
            break
        answer += 1
        k *= 2

    return answer