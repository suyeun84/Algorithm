import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split())
ks = list(map(int, input().strip().split()))
nums = []
result = set()

def brute():
    if nums:
        number = int(''.join(map(str, nums)))
        if n < number:
            return
        else:
            result.add(number)
    for num in ks:
        nums.append(num)
        brute()
        nums.pop()
        
brute()
result = sorted(result)
print(result[-1])