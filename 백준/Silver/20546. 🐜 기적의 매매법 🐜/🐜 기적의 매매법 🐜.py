money = int(input())

stock = list(map(int, input().split()))

jun = money
junstocknum = 0
for curr in stock:
    if(jun == 0):
        break
    if(jun >= curr):
        junstocknum += int(jun/curr)
        jun -= curr*int(jun/curr)
juntotal = stock[-1] * junstocknum + jun

sung = money
sungstocknum = 0
upcnt = 0
downcnt = 0
prev = stock[0]
for curr in stock:
    #상승중
    if(prev < curr):
        downcnt = 0
        upcnt += 1
        if upcnt == 3:
            sung += curr*sungstocknum
            sungstocknum = 0
    #하락중
    elif(prev > curr):
        upcnt = 0
        downcnt += 1
        if (downcnt >= 3) & (int(sung/curr) > 0):
            sungstocknum = sungstocknum + int(sung/curr)
            sung -= curr*int(sung/curr)
    elif(prev == curr):
        upcnt = 0
        downcnt = 0
    prev = curr
sungtotal = stock[-1] * sungstocknum + sung

if(juntotal < sungtotal):
    print("TIMING")
elif(juntotal > sungtotal):
    print("BNP")
else:
    print("SAMESAME")