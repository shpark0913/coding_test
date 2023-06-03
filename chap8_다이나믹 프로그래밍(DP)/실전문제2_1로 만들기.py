X = int(input())

dp = [0] * 30001

for i in range(2, X + 1):
    # 현재 값에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 3으로 나누어 떨어지는 경우
    if not i % 3:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    # 2로 나누어 떨어지는 경우
    if not i % 2:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    # 5로 나누어 떨어지는 경우
    if not i % 5:
        dp[i] = min(dp[i // 5] + 1, dp[i])

print(dp[X])