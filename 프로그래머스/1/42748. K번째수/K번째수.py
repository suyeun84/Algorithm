import sys
input = sys.stdin.readline

def solution(array, commands):
    result = []
    
    for com in commands:
        i, j, k = com
        result.append(sorted(array[i-1:j])[k-1])
    return result