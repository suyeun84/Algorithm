def solution(s1, s2):
    answer = 0
    for i in range(len(s2)):
        if s2[i] in s1:
            answer += 1
    return answer