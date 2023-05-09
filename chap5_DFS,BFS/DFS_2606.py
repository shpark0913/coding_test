# 백준 2606 (실버 3)
# https://www.acmicpc.net/problem/2606
# Python3 / 메모리 : 31256KB / 시간 : 48ms

# 컴퓨터의 수
computerNum = int(input())

# 간선의 개수
edgeNum = int(input())

# 연결 리스트
adjList = [[] for _ in range(computerNum + 1)]
visited = [False] * (computerNum + 1)

# 웜 바이러스에 감염된 컴퓨터의 수
virusCom = -1

for _ in range(edgeNum):
    s, e = map(int, input().split())
    adjList[s].append(e)
    if s not in adjList[e]:
        adjList[e].append(s)

def dfs(graph, v, visited):
    global virusCom
    visited[v] = True
    virusCom += 1
    if graph[1] == []:
        return 0
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return virusCom

print(dfs(adjList, 1, visited))
