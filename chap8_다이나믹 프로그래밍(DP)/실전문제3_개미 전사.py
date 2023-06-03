# 식량 창고의 수
N = int(input())

# 각 식량창고에 저장된 식량의 개수
storages = list(map(int, input().split()))

dp = [0] * 101

dp[1] = storages[0]
dp[2] = max(storages[0], storages[1])

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + storages[i - 1])

print(dp[N])