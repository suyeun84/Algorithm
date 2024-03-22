from collections import deque
def solution(s):
    answer = 0

    for i in range(len(s), 0, -1): #문자열 길이 설정해줌
        for start in range(0, len(s)+1-i): #start 위치 설정
            end = start + i
            str1 = s[start:end]
            if str1 == str1[::-1]:
                return i            
    return answer