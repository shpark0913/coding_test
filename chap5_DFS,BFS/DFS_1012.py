# 백준 1012 (실버 2)
# https://www.acmicpc.net/problem/1012
# Python3 / 메모리 : 31732KB / 시간 : 308ms

import sys
sys.setrecursionlimit(10**7)

T = int(input())  # 테스트 케이스의 수


def dfs(graph, isvisited, a, b):
    isvisited[a][b] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        nx = a + dx[k]
        ny = b + dy[k]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if (not isvisited[nx][ny]) and graph[nx][ny] == 1:
                dfs(graph, isvisited, nx, ny)


for t in range(T):
    M, N, K = map(int, input().split())   # 가로 길이, 세로 길이, 배추의 개수

    # 배추흰지렁이의 수
    bugNum = 0

    # 배추밭 (1: 배추, 0: 빈 위치)
    field = [[0] * N for _ in range(M)]

    # 방문 여부
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, input().split())  # 배추의 위치
        field[X][Y] = 1

    for i in range(len(field)):
        for j in range(len(field[0])):
            if (not visited[i][j]) and field[i][j] == 1:
                dfs(field, visited, i, j)
                bugNum += 1

    print(bugNum)