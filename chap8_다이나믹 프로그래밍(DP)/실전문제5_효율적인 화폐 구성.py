# N : 화폐의 종류, M : 가치의 합
N, M = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

dp = [10001] * (M + 1)

dp[0] = 0

for i in range(N):
    for j in range(coins[i], M + 1):
        if dp[j - coins[i]] != 10001:    # (i - k)원을 만드는 방법이 존재할 경우
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)


if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])