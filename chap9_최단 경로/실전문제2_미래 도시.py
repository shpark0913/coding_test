# 회사의 개수, 경로의 개수
N, M = map(int, input().split())

graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    graph[a][a] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

X, K = map(int, input().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][K] + graph[K][X]

print(-1) if distance >= int(1e9) else print(distance)