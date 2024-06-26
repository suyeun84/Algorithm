def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            if stack[-1] == "(":
                stack.pop()
    if len(stack) != 0:
        return False
    return True