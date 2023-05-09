# 백준 1388 (실버 4)
# https://www.acmicpc.net/problem/1388
# Python3 / 메모리 : KB / 시간 : ms

# 바닥의 세로 크기 : N, 가로 크기 : M
N, M = map(int, input().split())

floor = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(floor, i, j, visited):
    visited[i][j] = True
    if floor[i][j] == '-':
        if floor[i+1][j] and floor[i+1][j] == '-':
            dfs(floor, i + 1, j, visited)
    elif floor[i][j] == '|':
        if floor[i][j+1] and floor[i][j+1] == '|':
            dfs(floor, i, j + 1, visited)