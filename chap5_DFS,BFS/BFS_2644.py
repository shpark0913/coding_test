# 백준 2644 (실버 2)
# https://www.acmicpc.net/problem/2644
# Python3 / 메모리 : 31256KB / 시간 : 40ms
# PyPy3 / 메모리 초과
from collections import deque
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

cnt = 0
def dfs(V):
    for i in relations[V]:
        if visited[i] == 0:
           visited[i] = visited[V] + 1
           dfs(i)

dfs(a)

print(visited[b] if visited[b] else -1)

