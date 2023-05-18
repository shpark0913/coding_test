# 백준 2644 (실버 2)
# https://www.acmicpc.net/problem/2644
# Python3 / 메모리 : 34120KB / 시간 : 64ms
# PyPy3 / 메모리 : 114436KB / 시간 : 136ms
# BFS 풀이

import sys
from collections import deque

input = sys.stdin.readline

# 사람의 수
n = int(input())

a, b = map(int, input().split())

relations = [[] for _ in range(101)]
visited = [0 for _ in range(101)]

# 부모, 자식 관계의 수
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

def bfs(V):
    queue = deque([V])
    while queue:
        q = queue.popleft()
        for i in relations[q]:
            if not visited[i]:
                visited[i] = visited[q] + 1
                queue.append(i)

bfs(a)

print(visited[b] if visited[b] else -1)


###################################################
# Python3 / 메모리 : 31256KB / 시간 : 40ms
# PyPy3 / 메모리 초과
# DFS 풀이
import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline

# 사람의 수
n = int(input())

a, b = map(int, input().split())

relations = [[] for _ in range(101)]
visited = [0 for _ in range(101)]
# 부모, 자식 관계의 수
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

def dfs(V):
    for i in relations[V]:
        if visited[i] == 0:
           visited[i] = visited[V] + 1
           dfs(i)

dfs(a)

print(visited[b] if visited[b] else -1)

