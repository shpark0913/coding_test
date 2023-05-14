# 백준 4963 (실버 2)
# https://www.acmicpc.net/problem/4963
# Python3 / 메모리 : 34176KB / 시간 : 76ms
# PyPy3 / 메모리 : 116792KB / 시간 : 200ms

from collections import deque
import sys

input = sys.stdin.readline

def bfs(a, b):
    graph[a][b] = 0
    queue = deque([[a, b]])
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    while queue:
        q = queue.popleft()
        for k in range(8):
            nx = q[0] + dx[k]
            ny = q[1] + dy[k]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append(([nx, ny]))


while 1:
    # 지도의 너비와 높이
    w, h = map(int, input().split())
    if [w, h] == [0, 0]: break

    # 지도를 나타 내는 이중 리스트
    graph = []

    # 섬의 개수
    islands = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                islands += 1

    print(islands)

