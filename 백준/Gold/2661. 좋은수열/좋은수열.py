#좋은수열인지 여부 확인하는 함수
def check(nums, cnt):
    for i in range(cnt):
        slice_nums = nums[i:]
        for j in range(1,len(slice_nums)//2+1):
            if slice_nums[:j] == slice_nums[j:j+j]:
                return False
    return True

def backtracking(cnt):
    #좋은수열이면 nums에 추가 아니면 pass
    if not check(nums, cnt):
        return
    if cnt == n:
        print(*nums, sep='')
        return 1
    for i in range(1, 4):
        nums.append(i)
        if backtracking(cnt+1) == 1:
            return 1
        nums.pop()
        
n = int(input())
nums = []
backtracking(0)