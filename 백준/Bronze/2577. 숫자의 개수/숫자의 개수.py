A = int(input())
B = int(input())
C = int(input())
S = str(A * B * C)
result = [0]*10
for i in S:
    result[int(i)] += 1
for i in range(10):
    print(result[i])