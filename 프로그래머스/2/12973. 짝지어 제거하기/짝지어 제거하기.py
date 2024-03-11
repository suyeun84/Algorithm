def solution(s):
    stack = []    
    for a in s:
        if len(stack) == 0:
            stack.append(a)
            continue
        if stack:
            if stack[-1] == a:
                stack.pop()
            else:
                stack.append(a)
    if len(stack) == 0:
        return 1
    return 0