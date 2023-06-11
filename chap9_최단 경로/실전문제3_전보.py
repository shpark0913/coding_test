import heapq
import sys
input = sys.stdin.readline

# 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시
N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]

distance = [int(1e9)] * (N + 1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

cnt = -1
max_time = 0

for i in range(1, len(distance)):
    if distance[i] != int(1e9):
        cnt += 1
        max_time = max(max_time, distance[i])

print(cnt, max_time)
