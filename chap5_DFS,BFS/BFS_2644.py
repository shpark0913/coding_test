# 백준 2644 (실버 2)
# https://www.acmicpc.net/problem/2644
# Python3 / 메모리 : KB / 시간 : ms
# PyPy3 / 메모리 : KB / 시간 : ms

# 전략 : DFS 로 풀기
# DFS 계산해서 cnt가 가장 적은 순간을 답으로 할 것
# 단, -1 출력해야 하는 경우를 잘 생각할 것

def dfs(graph, visited, v, s):
    global cnt
    visited[v] = True
    if v == s:
        return cnt
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, visited, i)

# 전체 사람의 수
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())

# 부모 자식들 간의 관계의 개수
m = int(input())

relations = [[] for _ in range(101)]
visited = [[] for _ in range(101)]

cnt = 0

for _ in range(m):
    personA, personB = map(int, input().split())
    relations[personA].append(personB)
    relations[personB].append(personA)

print(dfs)