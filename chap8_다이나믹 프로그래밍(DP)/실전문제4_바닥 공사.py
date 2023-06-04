# 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 바닥
N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[N])