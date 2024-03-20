def solution(gems):
    answer = [1, len(gems)]
    gem = list(set(gems))
    n = len(gem)
    dis = 1e9
    
    dic = {gems[0]: 1}
    left, right = 0, 0
    
    while left <= right and left < len(gems):
        if len(dic) == n:
            if right-left < answer[1] - answer[0]:
                answer = [left+1, right+1]
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
                 
        elif len(dic) < n:
            right += 1
            if right >= len(gems):
                break
            if gems[right] in dic:
                dic[gems[right]] += 1
            else:
                dic[gems[right]] = 1

    return answer

