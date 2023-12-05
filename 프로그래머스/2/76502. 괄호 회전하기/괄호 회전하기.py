from collections import deque
def solution(s):
    answer = 0
    news = s + s
    for i in range(0, len(s)):
        tc = news[i: i+len(s)]
        st = deque()
        flag = True
        for a in tc:
            if a == "[" or a == "{" or a == "(":
                st.append(a)
            elif a == ")":
                if len(st)==0 or st.pop() != "(":
                    flag = False
                    continue
            elif a == "}":
                if len(st)==0 or st.pop() != "{":
                    flag = False
                    continue
            elif a == "]":
                if len(st)==0 or st.pop() != "[":
                    flag = False
                    continue
        if(flag == True and len(st)==0):
            answer += 1
    return answer