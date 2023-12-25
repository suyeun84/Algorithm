import sys

input = sys.stdin.readline

#최소 한 개의 모음 + 최소 두 개의 자음
#알파벳이 증가하는 순서로 배열

L, C = map(int, input().split())
words = sorted(list(map(str, input().split())))
result = []

def back_tracking(cnt, idx):
    if cnt == L:
        mo, ja = 0, 0
        
        for i in range(L):
            if result[i] in ['a', 'e', 'i', 'o', 'u']:
                mo += 1
            else:
                ja += 1
        if mo >= 1 and ja >= 2:
            print("".join(result))
        return
    
    for i in range(idx, C):
        result.append(words[i])
        back_tracking(cnt+1, i+1)
        result.pop()
        
back_tracking(0,0)