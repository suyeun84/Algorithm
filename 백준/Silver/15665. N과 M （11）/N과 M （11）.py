import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
result = {}

def dfs():
    if len(s) == m:
        if tuple(s) not in result:
            result[tuple(s)] = 1
            print(*s)
        return
    for i in nums:
        s.append(i)
        dfs()
        s.pop()
           
dfs()

#-------파이썬 내장함수------
#from itertools import product

#N, M = map(int, input().split())
#numlist = list(map(int, input().split()))
#case = sorted(set(product(numlist, repeat=M)))

#for i in case:
#    for j in i:
#        print(j, end=" ")
#    print()