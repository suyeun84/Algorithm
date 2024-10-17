import sys

def solution():
    input = sys.stdin.readline
    T = int(input())

    def dfs(num, res):
        if num == N:
            ans = eval(res.replace(' ', ''))
            if ans == 0:
                answer.append(res)
            return
        snum = num+1
        dfs(snum, res+' '+str(snum))
        dfs(snum, res+'+'+str(snum))
        dfs(snum, res+'-'+str(snum))

    for _ in range(T):
        answer = []
        N = int(input())
        dfs(1, '1')
        for a in answer:
            print(a)
        print()


if __name__ == '__main__':
    solution()
