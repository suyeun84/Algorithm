nk = input().split()
n = int(nk[0])
k = int(nk[1])

people = []
result = []
index = 0

for i in range(n):
    people.append(i+1)

while(len(people) > 0):
    result.append(str(people.pop((index + k - 1) % len(people))))
    index = (index + k - 1) % (len(people)+1)
print("<", ", ".join(result), ">", sep="")