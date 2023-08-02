S = input()
result = [-1]*26
for i in range(len(S)):
    if result[ord(S[i])-97] == -1:
        result[ord(S[i])-97] = i
for i in range(26):
    print(result[i], end=' ')