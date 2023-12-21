def hanoi(n, start, end):
    mid = 3-(start+end)
    if n == 1:
        print(start+1, end+1)
        return
    hanoi(n-1, start, mid)
    print(start+1, end+1)
    hanoi(n-1, mid, end)

n = int(input())
print(2**n-1)
hanoi(n,0,2)