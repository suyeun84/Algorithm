#2562
max_num = int(input())
result = 1
for i in range(2, 10):
    num = int(input())
    if num > max_num:
        max_num = num
        result = i
print(max_num)
print(result)