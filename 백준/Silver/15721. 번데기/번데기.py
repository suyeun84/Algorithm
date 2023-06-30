a = int(input())
t = int(input())
word = int(input())

round = 1
cnt = 0 #나온 단어 count
total = 0

up = 1
while(cnt < t):
    cnt = cnt + (3 + up)
    total += (6 + 2*up)
    up += 1
total = total - (6 + 2*(up-1))
cnt = cnt - (3 + (up-1))
num = t - cnt
if num == 1:
    if word == 0:
        total += 1
    else:
        total += 2
elif num == 2:
    if word == 0:
        total += 3
    else:
        total += 4
else:
    if word == 0:
        total += (4+num-2)
    else:
        total += (4+up+num-2)
            
print((total-1)%a)