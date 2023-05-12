from collections import deque

# 정점의 개수, 간선의 개수, 탐색 시작 정점 번호
N, M, V = map(int, input().split())

visited_DFS = [False] * (N + 1)
visited_BFS = [False] * (N + 1)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    if s not in graph[e]:
        graph[e].append(s)

for elt in graph:
    elt = sorted(elt)

def dfs(graph, visited, V):
    visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, visited, i)

# def bfs(graph, visited, V):
dfs(graph, visited_DFS, V)