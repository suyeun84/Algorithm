from collections import Counter
alpa = Counter(input().upper())
max_num = 0
max_str = ''

for i, j in alpa.items():
    if j > max_num:
        max_num = j
        max_str = i
    elif j == max_num:
        max_str = "?"
print(max_str)