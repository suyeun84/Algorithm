n, k = map(int, input().split())

#people = [i+1 for i in range(n)]
people = [i for i in range(1, n+1)]
result = []
index = 0

while people:
    index += k - 1
    if index >= len(people):
        index %= len(people)
    result.append(str(people.pop(index)))
    
print("<", ", ".join(result), ">", sep="")