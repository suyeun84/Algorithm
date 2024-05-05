arr=[]
result=[]
find_result=False
sum=0
for i in range(9):
    tmp=int(input())
    arr.append(tmp)
    sum+=tmp


for i in range(9):
    for j in range(i+1,9):
        tmp_sum=sum-arr[i]-arr[j]
        if tmp_sum==100:
            result.extend([arr[i],arr[j]])
            find_result=True
            break
    if find_result:break


arr.sort()
for ele in arr:
    if ele not in result:print(ele)