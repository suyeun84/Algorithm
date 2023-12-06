def solution(triangle):
    answer = 0
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    #깊이에 따라 계속 더하기
    dp[0][0] = triangle[0][0]
    
    for floor in range(1, len(triangle)):
        for col in range(0, floor+1):
            if col == 0:
                dp[floor][col] = dp[floor-1][0] + triangle[floor][col]
            elif col == floor:
                dp[floor][col] = dp[floor-1][col-1] + triangle[floor][col]
            else:
                dp[floor][col] = max(dp[floor-1][col-1], dp[floor-1][col])+triangle[floor][col]
            
    return max(dp[len(triangle)-1])