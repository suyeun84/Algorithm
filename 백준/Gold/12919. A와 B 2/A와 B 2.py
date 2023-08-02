import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
result = 0

#T를 S로 만들기
def brute(curr):
    global result
    #break 조건 설정해주기
    if len(curr) == 0:
        return
    if curr == S:
        result = 1
        return
    #문자열 맨뒤 A면 A 삭제
    if curr[-1] == 'A':
        brute(curr[:-1])
    #문자열 맨앞 B면 삭제하고 reverse
    if curr[0] == 'B':
        brute(curr[1:][::-1])
        
brute(T)
print(result)