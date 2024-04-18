def solution(sequence):
    dp = [sequence[i] * (-1) if i % 2 == 0 else sequence[i] for i in range(len(sequence))]
    dp2 = [sequence[i] if i % 2 == 0 else sequence[i] * (-1) for i in range(len(sequence))]

    for i in range(1, len(sequence)):
        dp[i] = max(dp[i], dp[i-1]+dp[i])
        dp2[i] = max(dp2[i], dp2[i-1]+dp2[i])
    return max(max(dp), max(dp2))