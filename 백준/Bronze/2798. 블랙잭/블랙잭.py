n, m = map(int, input().split())

result = 0
card = list(map(int, input().split()))

for i in range(len(card)):
    for j in range(i+1, len(card)):
        for z in range(j+1, len(card)):
            if(card[i]+card[j]+card[z] == m):
                result = m
                break
            elif(card[i]+card[j]+card[z] < m):
                result = max(result, card[i]+card[j]+card[z])
        else:
            continue
        break
    else:
        continue
    break
print(result)