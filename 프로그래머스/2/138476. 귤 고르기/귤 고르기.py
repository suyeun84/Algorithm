def solution(k, tangerine):
    dic = {}
    answer = 0
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    for i in dic:
        if k > 0:
            answer += 1
            k -= i[1]
        else:
            break
    return answer
            