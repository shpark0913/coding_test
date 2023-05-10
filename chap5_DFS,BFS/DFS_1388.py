# 백준 1388 (실버 4)
# https://www.acmicpc.net/problem/1388
# Python3 / 메모리 : 31256KB / 시간 : 52ms
# input = sys.stdin.readline 하면 시간 : 44ms

# 바닥의 세로 크기 : N, 가로 크기 : M
N, M = map(int, input().split())

floor = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 필요한 나무 판자의 개수
boardNum = 0

def dfs(floor, visited, i, j):
    global boardNum
    # 방문 처리
    visited[i][j] = True
    boardNum += 1

    if floor[i][j] == '-':
        while 1:
            if j + 1 < M and floor[i][j+1] == '-':
                visited[i][j+1] = True
                j += 1
            else:
                break
    elif floor[i][j] == '|':
        while 1:
            if i + 1 < N and floor[i+1][j] == '|':
                visited[i+1][j] = True
                i += 1
            else:
                break


for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            dfs(floor, visited, i, j)

print(boardNum)