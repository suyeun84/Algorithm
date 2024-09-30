import sys

def solution():
    input = sys.stdin.readline
    T = int(input())
    dic = {}
    for _ in range(T):
        W = input().strip()
        K = int(input())
        answer = []
        for i in range(len(W)):
            if W[i] not in dic:
                dic[W[i]] = [i]
            else:
                dic[W[i]].append(i)
            if len(dic[W[i]]) == K:
                answer.append(i - dic[W[i]][0] + 1)
                del dic[W[i]][0]
        dic.clear()
        if len(answer) == 0:
            print(-1)
            continue
        answer.sort()
        print(answer[0], answer[-1])
        

if __name__ == '__main__':
    solution()
