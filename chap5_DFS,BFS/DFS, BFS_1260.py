# 백준 1260 (실버 2)
# https://www.acmicpc.net/problem/1260
# Python3 / 메모리 : 34176KB / 시간 : 468ms
# PyPy3 / 메모리 : 117424KB / 시간 : 196ms

from collections import deque

# 정점의 개수, 간선의 개수, 탐색 시작 정점 번호
N, M, V = map(int, input().split())

visited_DFS = [False] * (N + 1)
visited_BFS = [False] * (N + 1)

result_DFS = []
result_BFS = []

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for elt in graph:
    elt.sort()

def dfs(graph, visited, V):
    global result_DFS
    visited[V] = True
    result_DFS.append(V)
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, visited, V):
    global result_BFS
    Queue = deque([V])
    visited[V] = True
    while Queue:
        q = Queue.popleft()
        result_BFS.append(q)
        for elt in graph[q]:
            if not visited[elt]:
                visited[elt] = True
                Queue.append(elt)


dfs(graph, visited_DFS, V)
bfs(graph, visited_BFS, V)

print(*result_DFS)
print(*result_BFS)