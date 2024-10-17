import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    answer = set()
    nums = [-1]
    for _ in range(N):
        nums.append(int(input()))

    def dfs(idx, res, curr):
        idx.add(curr)
        res.add(nums[curr])
        if nums[curr] in idx:
            if idx == res:
                answer.update(idx)
                return True
            return False
        return dfs(idx, res, nums[curr])

    for i in range(1, N+1):
        if i not in answer:
            dfs(set(), set(), i)

    print(len(answer))
    print(*sorted(answer), sep='\n')


if __name__ == '__main__':
    solution()
